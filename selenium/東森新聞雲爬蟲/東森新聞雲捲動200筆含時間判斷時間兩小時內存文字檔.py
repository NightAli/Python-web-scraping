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
# 註解（自動）：從 wordcloud 匯入 WordCloud, ImageColorGenerator
from wordcloud import WordCloud, ImageColorGenerator
# 註解（自動）：匯入 jieba
import jieba
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
