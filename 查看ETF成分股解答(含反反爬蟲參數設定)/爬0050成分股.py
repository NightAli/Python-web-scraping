'''
需先安裝套件
pip3 install selenium
pip3 install BeautifulSoup4
pip3 install pandas
pip3 install wordcloud
pip3 install jieba
pip3 install matplotlib
pip3 install numpy
並將chromedriver與程式碼放在同一個資料夾中
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions   #20230623新增
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import numpy as np
from collections import Counter
chrome_options = Options()

# 讓瀏覽器在關閉程式後不自動關閉（非防爬，但方便除錯）
chrome_options.add_experimental_option("detach", True)

# 使用一般使用者的 User-Agent（模仿常見瀏覽器）
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

# 避免被識別為自動化工具
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# 禁用 "Chrome is being controlled by automated test software" 的提示
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# 啟用無頭模式可選擇性加入，但更容易被發現為機器人
# chrome_options.add_argument("--headless=new")

# 模擬人類的視窗大小和設備解析度
chrome_options.add_argument("--window-size=1280,800")

# 禁用圖片載入（加快速度，不一定必要）
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(options=chrome_options)

# 執行防爬處理（最重要的一步）：修改 navigator.webdriver 為 False
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """
})
browser.get("https://www.wantgoo.com/stock/etf/0050/constituent") #用虛擬瀏覽器開啟指定網址
time.sleep(5) #等待2秒
html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
bigarea=soup.find("tbody",id="holdingTable")
#print(bigarea.text)
area=bigarea.find_all("tr")
#print(area[0].find_all("td")[0].text)
for i in area:
    print(i.find_all("td")[0].text)

browser.close() #關閉瀏覽器