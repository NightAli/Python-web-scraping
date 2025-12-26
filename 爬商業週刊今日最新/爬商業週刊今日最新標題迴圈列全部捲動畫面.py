# 註解（自動）：從 selenium 匯入 webdriver
from selenium import webdriver
# 註解（自動）：從 selenium.webdriver.chrome.options 匯入 Options
from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023改版
# 註解（自動）：從 bs4 匯入 BeautifulSoup
from bs4 import BeautifulSoup
# 註解（自動）：從 datetime 匯入 datetime, timedelta
from datetime import datetime, timedelta
# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：匯入 xlsxwriter
import xlsxwriter
# 註解（自動）：匯入 time
import time
# 註解（自動）：從 datetime 匯入 datetime, timedelta
from datetime import datetime,timedelta

#設定瀏覽器驅動程式與爬蟲網址
chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://www.businessweekly.com.tw/latest?p=2")

#捲動瀏覽器
last_height=browser.execute_script("return document.body.scrollHeight") #目前視窗高度
browser.execute_script("window.scrollTo(0,"+str(last_height)+");")  #捲動視窗方法1
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight);") #捲動視窗方法2
time.sleep(8)

html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("figure",class_="Article-figure d-xs-flex")
# 註解（自動）：對 i  在 area1 中迭代
for i in area1:
    article=i.find("div",class_="Article-content d-xs-flex")
    print(article.text)

browser.close()
