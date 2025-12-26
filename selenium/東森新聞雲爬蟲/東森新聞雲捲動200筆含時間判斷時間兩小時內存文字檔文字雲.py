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
# 註解（自動）：從 selenium 匯入 webdriver
from selenium import webdriver
# 註解（自動）：從 selenium.webdriver.chrome.options 匯入 Options
from selenium.webdriver.chrome.options import Options as ChromeOptions   #20230623新增
# 註解（自動）：從 bs4 匯入 BeautifulSoup
from bs4 import BeautifulSoup
# 註解（自動）：從 datetime 匯入 datetime, timedelta
from datetime import datetime, timedelta
# 註解（自動）：匯入 time
import time
# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：從 PIL 匯入 Image
from PIL import Image
# 註解（自動）：匯入 matplotlib.pyplot
import matplotlib.pyplot as plt
# 註解（自動）：從 wordcloud 匯入 WordCloud, ImageColorGenerator, STOPWORDS
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
# 註解（自動）：匯入 jieba
import jieba
# 註解（自動）：匯入 jieba.analyse
import jieba.analyse
# 註解（自動）：匯入 numpy
import numpy as np
# 註解（自動）：從 collections 匯入 Counter
from collections import Counter


#20230623 selenium4 改版後呼叫方式
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.ettoday.net/news/news-list.htm") #用虛擬瀏覽器開啟指定網址
time.sleep(2) #等待載入畫面2秒


#for j in range(0,1):  #發現基本頁面100筆,每次捲頁新增20筆,故捲動10次即可獲得200筆
hour2=2 #捲2小時內
flag1=False #是否時間達標
# 註解（自動）：當條件成立時重複執行
while True: #無限捲頁
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight*0.9);") #捲動視窗一整頁
    time.sleep(1) #等待1秒
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight*0.7);") #捲動視窗一整頁
    time.sleep(1) #等待1秒
    #---------爬蟲檢查指定時間
    html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
    soup=BeautifulSoup(html_source,"lxml")
    bigarea=soup.find(class_="part_list_2")
    area=bigarea.find_all("h3")
# 註解（自動）：對 i  在 area 中迭代
    for i in area:
        time1=i.find("span").text
        dt1=datetime.strptime(time1,'%Y/%m/%d %H:%M') #將網頁上的時間轉換成電腦時間變數
        hour1=datetime.now()-timedelta(hours=hour2) #現在時間扣幾小時
        print(dt1,hour1)
# 註解（自動）：若 dt1 < hour1
        if dt1<hour1: #比對是否幾小時前
            flag1=True #設定時間達標
            break
# 註解（自動）：若 flag1 == True
    if flag1==True: #時間達標離開無限捲頁
        break

html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
bigarea=soup.find(class_="part_list_2")
area=bigarea.find_all("h3")
total=0 #計算筆數
content1="" #宣告空的總標題內容
# 註解（自動）：對 i  在 area 中迭代
for i in area:
    time1=i.find("span").text
    print(time1,end="")  #顯示時間
    title1=i.find("a").text
    print(title1)  #顯示標題
    content1=content1+title1
    total=total+1
    dt1=datetime.strptime(time1,'%Y/%m/%d %H:%M') #將網頁上的時間轉換成電腦時間變數
    hour1=datetime.now()-timedelta(hours=hour2) #現在時間扣幾小時
# 註解（自動）：若 dt1 < hour1
    if dt1<hour1: #比對是否幾小時前
        break
    
print("總筆數:",total)
browser.close() #關閉瀏覽器
with open('etnews.txt','w',encoding="utf-8") as file:  #開一個純文字檔案保存
    file.write(content1) #寫入總標題內容
    
    
dictfile = "dict.txt.big.txt"  #設定常用字典
stopfile = "stopWord.txt"  #設定停用詞，譬如唱歌會用到的oh，喔
fontpath = "msjh.ttf"  #中文繪圖需要中文字體,微軟正黑體
userdict="userdict.txt" #設定自訂的字典,就是一定要保留的，譬如五月天的 "動次"
mdfile = "etnews.txt"  #要分析的來源，這個範例是五月天20首歌
topwords=50 #使用排名前幾個的字詞
pngfile = "cloud.jpg"  #想要文字雲出現的遮罩圖案(單色,png檔案背景不可透明)
outputfile="Mayday_Wordcloud.png"  #輸出圖片檔案名稱

bgmask = np.array(Image.open(pngfile))

jieba.set_dictionary(dictfile)
jieba.analyse.set_stop_words(stopfile)
jieba.load_userdict(userdict)
text = open(mdfile,"r",encoding="utf-8").read()
tags = jieba.analyse.extract_tags(text, topK=topwords)
seg_list = jieba.lcut(text, cut_all=False)
dictionary = Counter(seg_list)

#開始段詞與排序
freq = {}
# 註解（自動）：對 ele  在 dictionary 中迭代
for ele in dictionary:
# 註解（自動）：若 ele in tags
    if ele in tags:
        freq[ele] = dictionary[ele]
print(freq) # 計算各詞彙出現的次數

#背景顏色預設黑色，改為白色
#遮罩圖案改用五月天的皇冠
#contour是指邊框
#margin是文字間距
#其他參數請自行參考wordcloud
wordcloud = WordCloud(background_color="white", mask=bgmask, contour_width=3, contour_color='steelblue', font_path= fontpath).generate_from_frequencies(freq)
#wordcloud = WordCloud(background_color="white", mask=bgmask, font_path= fontpath, width=2400, height=2400, margin=0).generate_from_frequencies(freq)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
#存檔用
plt.savefig(outputfile)
#顯示用
plt.show()
