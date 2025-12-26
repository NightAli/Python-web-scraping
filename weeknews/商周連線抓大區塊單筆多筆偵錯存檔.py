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


browser.get("https://www.businessweekly.com.tw/latest?p=1") #用虛擬瀏覽器開啟指定網址
time.sleep(2) #等待2秒

html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
bigarea=soup.find("div",id="searchResult")
#print(bigarea.text)
area=bigarea.find_all("figure")
print(area[0])

#定義資料框架
df=pd.DataFrame(columns=["標題","撰文","時間","連結"])

total=0
# 註解（自動）：對 i  在 area 中迭代
for i in area:
# 註解（自動）：嘗試區塊（try/except/finally）
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
        df.loc[total]=[title1,author1,time1,link1]
        total=total+1
    except:
        print("error")
# 註解（自動）：若 total >= 10
    if total>=10: #顯示10筆
        break
print("總筆數:",total)

browser.close() #關閉瀏覽器

#存成excel
writer=pd.ExcelWriter("weeknews.xlsx",engine='xlsxwriter') #開啟檔案
df.to_excel(writer,sheet_name="商周",index=False) #寫入資料到指定工作表去索引欄位
writer.close() #關閉檔案
