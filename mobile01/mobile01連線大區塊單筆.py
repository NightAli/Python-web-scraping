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
# Auto-annotated: from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

#20230623 selenium4 改版後呼叫方式
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)


browser.get("https://www.mobile01.com/hottopics.php?id=6") #用虛擬瀏覽器開啟指定網址
time.sleep(2) #等待2秒



html_source=browser.page_source  #載入瀏覽器所看到的網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
bigarea=soup.find("div",class_="l-listTable__tbody")
#print(bigarea.text)
area=bigarea.find_all("div",class_="l-listTable__tr")
print(area[0]) #單筆資料



browser.close() #關閉瀏覽器

