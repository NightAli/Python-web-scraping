from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023改版
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import xlsxwriter
import time
from datetime import datetime,timedelta

#設定瀏覽器驅動程式與爬蟲網址
chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://www.businessweekly.com.tw/latest?p=2")
time.sleep(5)

html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("figure",class_="Article-figure d-xs-flex")
for i in area1:
    article=i.find("div",class_="Article-content d-xs-flex")
    print(article.text)

browser.close()