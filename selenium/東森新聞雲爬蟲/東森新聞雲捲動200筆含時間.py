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

browser.get("https://www.ettoday.net/news/news-list.htm") #用虛擬瀏覽器開啟指定網址
time.sleep(2) #等待載入畫面2秒

for j in range(0,10):  #發現基本頁面100筆,每次捲頁新增20筆,故捲動10次即可獲得200筆
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight*0.9);") #捲動視窗一整頁
    time.sleep(1) #等待1秒
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight*0.7);") #捲動視窗一整頁
    time.sleep(1) #等待1秒

html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
bigarea=soup.find(class_="part_list_2")
area=bigarea.find_all("h3")
total=0
for i in area:
    time1=i.find("span").text
    print(time1,end="")  #顯示時間
    title1=i.find("a").text
    print(title1)  #顯示標題
    total=total+1
print("總筆數:",total)
browser.close() #關閉瀏覽器
