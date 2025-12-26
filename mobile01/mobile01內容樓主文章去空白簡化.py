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
from selenium.webdriver.common.by import By

chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.mobile01.com/topicdetail.php?f=294&t=7156777") #用虛擬瀏覽器開啟指定網址
time.sleep(2) #等待2秒
html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
bigarea=soup.find("div",class_="u-gapNextV--lg")
area=bigarea.find_all("div",class_="l-articlePage")
content1=area[0].find("article",class_="l-publishArea topic_article").text.replace(" ","").replace("\n","")
print(content1) #樓主文章
browser.close() #關閉瀏覽器
