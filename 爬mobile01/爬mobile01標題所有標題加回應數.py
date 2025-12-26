from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023
from selenium.webdriver.support.ui import Select
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
browser.get("https://www.mobile01.com/hottopics.php?id=6")
time.sleep(5)

#捲動瀏覽器
last_height=browser.execute_script("return document.body.scrollHeight") #目前視窗高度
print("舊視窗高度:",last_height)
b1=3 #紀錄按下"顯示更多"倒數次數
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight*0.8);") #捲動視窗方法2
    time.sleep(3)
    new_height=browser.execute_script("return document.body.scrollHeight") #目前視窗高度
    print("新視窗高度:",new_height)
    
   
    
    if new_height==last_height:
        print("捲到底了")
        break
    else:
        last_height=new_height  #紀錄目前高度




html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("div",class_="l-listTable__tr")
for i in range(1,len(area1),1):
    title=area1[i].find("div",class_="c-listTableTd__title")
    title2=title.find("a")
    rno=area1[i].find("div",class_="o-fMini")
    print(title2.text,rno.text)

browser.close()