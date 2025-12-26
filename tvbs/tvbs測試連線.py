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


browser.get("https://news.tvbs.com.tw/realtime") #用虛擬瀏覽器開啟指定網址
time.sleep(2) #等待2秒
#browser.close() #關閉瀏覽器
