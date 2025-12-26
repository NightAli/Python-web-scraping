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
# 註解（自動）：從 selenium.webdriver.common.by 匯入 By
from selenium.webdriver.common.by import By

# 註解（自動）：函式 getcontent1(url)
def getcontent1(url):    #定義抓樓主文章函式
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=chrome_options)

    browser.get(url) #用虛擬瀏覽器開啟指定網址
    time.sleep(2) #等待2秒
    html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
    soup=BeautifulSoup(html_source,"lxml")
    bigarea=soup.find("div",class_="u-gapNextV--lg")
    area=bigarea.find_all("div",class_="l-articlePage")
    content1=area[0].find("article",class_="l-publishArea topic_article").text.replace(" ","").replace("\n","")
    #print(content1) #樓主文章
    browser.close() #關閉瀏覽器
    return content1

#print(getcontent1("https://www.mobile01.com/topicdetail.php?f=294&t=7156777"))
