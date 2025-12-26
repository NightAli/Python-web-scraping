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

#20230623 selenium4 改版後呼叫方式
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)


browser.get("https://www.businessweekly.com.tw/latest?p=1") #用虛擬瀏覽器開啟指定網址
time.sleep(2) #等待2秒

html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
bigarea=soup.find("div",id="searchResult")
#print(bigarea.text)
area=bigarea.find_all("figure")
print(area[0])

total=0
for i in area:
    try:
        title1=i.find_all("a")[1].text #標題
        author1=i.find("span",class_="Article-author d-xs-none d-sm-inline").text #撰文者
        time1=i.find("span",class_="Article-date d-xs-none d-sm-inline").text #時間
        link1="https://www.businessweekly.com.tw"+i.find_all("a")[1].get("href") #超連結
        print("標題:",title1)
        print("撰文:",author1)
        print("時間:",time1)
        print("連結:",link1)
        print("------------------------------------")
        #df.loc[total]=[title1,author1,time1,link1]
        total=total+1
    except:
        print("error")
    if total>=10: #顯示10筆
        break
print("總筆數:",total)



browser.close() #關閉瀏覽器
