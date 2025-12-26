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
# Auto-annotated: from selenium import webdriver
from selenium import webdriver
# Auto-annotated: from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions   #20230623新增
# Auto-annotated: from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
# Auto-annotated: from datetime import datetime, timedelta
from datetime import datetime, timedelta
# Auto-annotated: imports time
import time
# Auto-annotated: imports pandas
import pandas as pd
# Auto-annotated: from PIL import Image
from PIL import Image
# Auto-annotated: imports matplotlib.pyplot
import matplotlib.pyplot as plt
# Auto-annotated: from wordcloud import WordCloud, ImageColorGenerator
from wordcloud import WordCloud, ImageColorGenerator
# Auto-annotated: imports jieba
import jieba
# Auto-annotated: imports numpy
import numpy as np
# Auto-annotated: from collections import Counter
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
# Auto-annotated: for i in area
for i in area:
# Auto-annotated: try/except/finally block
    try:
        title1=i.find_all("a")[1].text #標題
        author1=i.find("span",class_="Article-author d-xs-none d-sm-inline").text.replace("撰文者：","") #撰文者
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
# Auto-annotated: if total >= 10
    if total>=10: #顯示10筆
        break
print("總筆數:",total)

browser.close() #關閉瀏覽器

#存成excel
writer=pd.ExcelWriter("weeknews.xlsx",engine='xlsxwriter') #開啟檔案
df.to_excel(writer,sheet_name="商周",index=False) #寫入資料到指定工作表去索引欄位
writer.close() #關閉檔案
