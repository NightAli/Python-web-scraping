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
# Auto-annotated: from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

# Auto-annotated: function getcontent1(url)
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

print(getcontent1("https://www.mobile01.com/topicdetail.php?f=294&t=7156777"))
