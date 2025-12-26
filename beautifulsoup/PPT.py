import time  # 控制爬蟲請求節奏
import requests  # 發送 HTTP 請求到 PTT
import pandas as pd  # 將結果整理成表格輸出
from bs4 import BeautifulSoup  # 解析 HTML 內容


def normalize_push_count(push_text: str) -> int:  # 將推文顯示文字轉為數值
    # 將 PTT 列表頁的推文顯示文字轉成數值  # 功能說明
    # - '爆' -> 100  # 特例：爆文
    # - 'X1' -> -1  # 特例：噓文
    # - ''   -> 0  # 空字串視為 0
    # - '12' -> 12  # 一般數字
    if not push_text:  # 空字串直接回傳 0
        return 0  # 沒推文

    push_text = push_text.strip()  # 去掉前後空白

    if push_text == "爆":  # 爆文顯示
        return 100  # 固定視為 100

    # 例如 X1, X2...  # 噓文格式
    if push_text.startswith("X"):  # 判斷是否為噓文
        try:  # 嘗試解析噓文數字
            return -int(push_text[1:])  # 轉成負數
        except:  # 解析失敗就回 0
            return 0  # 異常時視為 0

    try:  # 一般數字推文
        return int(push_text)  # 直接轉 int
    except:  # 轉換失敗就回 0
        return 0  # 非數字時視為 0


def fetch_article_content(session: requests.Session, url: str, headers: dict, delay: float = 0.3) -> str:  # 抓取文章內文
    # 進入文章頁抓內文，並做基本清理  # 功能說明
    # - 移除作者/標題/時間等 meta 資訊  # 清理標頭
    # - 移除推文區塊  # 清掉推文
    # - 切掉「※ 發信站:」之後的系統資訊  # 去除系統尾巴
    try:  # 捕捉連線或解析錯誤
        res = session.get(url, headers=headers, timeout=10)  # 送出請求
        if res.status_code != 200:  # 非 200 表示失敗
            return f"N/A (文章頁狀態碼 {res.status_code})"  # 回傳錯誤訊息

        soup = BeautifulSoup(res.text, "html.parser")  # 解析 HTML
        main = soup.find("div", id="main-content")  # 找內文主區塊
        if not main:  # 找不到主區塊
            return "N/A (找不到 main-content)"  # 回傳提示

        # 移除 meta 資訊與推文  # 先清掉雜訊
        for tag in main.select("div.article-metaline, div.article-metaline-right, div.push"):  # 將不需要的區塊移除
            tag.decompose()  # 從 DOM 中刪除

        text = main.get_text("\n", strip=True)  # 取得清理後文字

        # 切掉常見尾巴  # 去掉系統訊息
        if "※ 發信站:" in text:  # 發信站標記
            text = text.split("※ 發信站:")[0].strip()  # 取前段
        if "--" in text:  # 簽名檔分隔
            # 有些文章會用 -- 當簽名檔分隔  # 說明
            text = text.split("--")[0].strip()  # 取前段

        time.sleep(delay)  # 控制請求間隔
        return text.strip() if text.strip() else "N/A (內文為空)"  # 空內容則標記

    except Exception as e:  # 捕捉例外
        return f"N/A (抓取內文失敗: {e})"  # 回傳失敗原因


def scrape_ptt_movie(pages: int,  # 要爬的頁數
                     with_content: bool = True,  # 是否進文章抓內文
                     page_delay: float = 1.0,  # 翻頁間隔秒數
                     article_delay: float = 0.3) -> list:  # 內文抓取間隔秒數
    # 爬取 PTT 電影版指定頁數  # 功能說明
    # - 過濾置底文  # 排除置底
    # - 擷取：標題、作者、日期、推文數、連結  # 欄位清單
    # - 可選：進入文章抓內文  # 內文選項
    base_url = "https://www.ptt.cc"  # PTT 網域
    url = f"{base_url}/bbs/movie/index.html"  # 起始頁網址

    headers = {  # HTTP 標頭
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "  # 偽裝瀏覽器
                      "AppleWebKit/537.36 (KHTML, like Gecko) "  # 瀏覽器內核
                      "Chrome/91.0.4472.124 Safari/537.36"  # 瀏覽器版本
    }  # 標頭結束

    session = requests.Session()  # 建立共用 Session
    session.cookies.set("over18", "1")  # 通過 18 禁提示

    all_articles_data = []  # 收集所有文章資料

    print(f"準備開始爬取 PTT 電影版，共 {pages} 頁...（with_content={with_content}）")  # 顯示進度

    for i in range(pages):  # 逐頁爬取
        print(f"\n正在爬取第 {i + 1} 頁: {url}")  # 顯示目前頁

        res = session.get(url, headers=headers, timeout=10)  # 取得頁面
        if res.status_code != 200:  # 失敗就中止
            print(f"錯誤：無法訪問頁面，狀態碼 {res.status_code}")  # 顯示錯誤
            break  # 結束迴圈

        soup = BeautifulSoup(res.text, "html.parser")  # 解析 HTML
        articles = soup.find_all("div", class_="r-ent")  # 找出文章區塊

        for article in articles:  # 逐篇處理
            # === p03：過濾置底文 ===  # 規則說明
            classes = article.get("class", [])  # 取得文章區塊 class
            if "r-ent-pinned" in classes:  # 置底文判斷
                title_text = article.find("div", class_="title").get_text(strip=True)  # 取得標題
                print(f"  (跳過置底文: {title_text})")  # 顯示被跳過
                continue  # 跳過置底文

            # 標題與連結  # 欄位說明
            title_tag = article.find("div", class_="title")  # 取得標題區塊
            if title_tag and title_tag.a:  # 有連結才是正常文章
                title = title_tag.a.get_text(strip=True)  # 取得標題文字
                article_url = base_url + title_tag.a["href"]  # 組合完整連結
            else:  # 沒有連結代表被刪除
                # 被刪除的文章通常沒有 <a>  # 補充說明
                title = "N/A (本文已被刪除)"  # 設定刪除提示
                article_url = "N/A"  # 無連結

            # 作者  # 欄位說明
            author_tag = article.find("div", class_="author")  # 取得作者區塊
            author = author_tag.get_text(strip=True) if author_tag else "N/A"  # 作者文字

            # 日期  # 欄位說明
            date_tag = article.find("div", class_="date")  # 取得日期區塊
            date = date_tag.get_text(strip=True) if date_tag else "N/A"  # 日期文字

            # === p02：推文數（列表頁可直接拿）===  # 推文處理
            nrec_tag = article.find("div", class_="nrec")  # 推文顯示區塊
            push_raw = nrec_tag.get_text(strip=True) if nrec_tag else ""  # 原始推文文字
            push_count = normalize_push_count(push_raw)  # 轉成數值

            # === p02：內文（進入文章頁抓）===  # 內文處理
            content = "N/A"  # 預設內文
            if with_content and article_url != "N/A":  # 需要內文且有連結
                content = fetch_article_content(  # 呼叫內文抓取
                    session=session,  # 共用 Session
                    url=article_url,  # 文章連結
                    headers=headers,  # 請求標頭
                    delay=article_delay  # 抓取延遲
                )  # 內文抓取結束

            all_articles_data.append({  # 整理欄位
                "標題": title,  # 標題
                "作者": author,  # 作者
                "日期": date,  # 日期
                "推文顯示": push_raw if push_raw else "0",  # 原始推文
                "推文數": push_count,  # 推文數值
                "連結": article_url,  # 文章網址
                "內文": content  # 文章內文
            })  # 單篇資料結束

        # 找上一頁  # 翻頁處理
        prev_page_link = soup.find("a", string="‹ 上頁")  # 上一頁連結
        if prev_page_link and prev_page_link.get("href"):  # 確認有連結
            url = base_url + prev_page_link["href"]  # 更新 URL
        else:  # 沒有上一頁
            print("找不到上一頁的連結，爬取結束。")  # 顯示訊息
            break  # 結束迴圈

        time.sleep(page_delay)  # 翻頁延遲

    return all_articles_data  # 回傳結果


if __name__ == "__main__":  # 主程式入口
    PAGES_TO_SCRAPE = 5  # 預設要爬的頁數

    scraped_data = scrape_ptt_movie(  # 呼叫爬蟲
        pages=PAGES_TO_SCRAPE,  # 頁數設定
        with_content=True,     # 進文章抓內文
        page_delay=1.0,        # 翻頁延遲
        article_delay=0.3      # 內文延遲
    )  # 爬蟲結束

    if scraped_data:  # 有抓到資料
        df = pd.DataFrame(scraped_data)  # 建立 DataFrame
        csv_filename = "ptt_movie.csv"  # 輸出檔名
        df.to_csv(csv_filename, index=False, encoding="utf-8-sig")  # 寫入 CSV

        print(f"\n爬取完成！共擷取 {len(scraped_data)} 篇文章。")  # 完成訊息
        print(f"資料已儲存至 {csv_filename}")  # 儲存位置
        print("\n前 5 筆資料預覽：")  # 預覽提示
        print(df.head())  # 顯示前五筆
    else:  # 沒有資料
        print("未取得任何資料。")  # 提示失敗
