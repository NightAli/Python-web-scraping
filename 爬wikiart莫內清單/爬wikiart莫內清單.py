# 註解（自動）：從 selenium.webdriver.common.keys 匯入 Keys
from selenium.webdriver.common.keys import Keys
# 註解（自動）：從 selenium.webdriver 匯入 DesiredCapabilities
from selenium.webdriver import DesiredCapabilities
# 註解（自動）：從 selenium.common.exceptions 匯入 NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
# 註解（自動）：從 selenium.webdriver.support.wait 匯入 WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
# 註解（自動）：從 selenium.webdriver.support 匯入 expected_conditions
from selenium.webdriver.support import expected_conditions as EC
# 註解（自動）：從 selenium.webdriver.common.by 匯入 By
from selenium.webdriver.common.by import By
# 註解（自動）：從 selenium.webdriver.common.action_chains 匯入 ActionChains
from selenium.webdriver.common.action_chains import ActionChains
# 註解（自動）：從 selenium 匯入 webdriver
from selenium import webdriver
# 註解（自動）：從 selenium.webdriver.chrome.options 匯入 Options
from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023
# 註解（自動）：從 selenium.webdriver.support.ui 匯入 Select
from selenium.webdriver.support.ui import Select
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
browser.get("https://www.wikiart.org/en/claude-monet/all-works/text-list")
time.sleep(5)


#宣告變數值
df=pd.DataFrame(columns=["作品名稱","作品年份"])  #宣告空的df
x=0

#爬大區塊
html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("li",class_="painting-list-text-row")   
#print(area1[0]text)                                     


#爬細節
# 註解（自動）：對 i  在 range(0, len(area1), 1) 中迭代
for i in range(0,len(area1),1):
    name1=area1[i].find("a").text
    year1=area1[i].find("span").text.replace(", ","")
    #if i>50:break
    
    print("作品名稱:",name1)
    print("作品年份:",year1)
    print("------------------")

    df.loc[x]=[name1,year1]  #紀錄存到pandas
    x=x+1


browser.close()


#儲存成檔案
#df.to_csv("momolist.csv",encoding="utf_8_sig")  #存成csv
#存成excel
writer=pd.ExcelWriter("momolist.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="mobile01")
writer.close()
