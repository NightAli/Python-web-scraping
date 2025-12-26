# Auto-annotated: from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
# Auto-annotated: from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import DesiredCapabilities
# Auto-annotated: from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
# Auto-annotated: from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
# Auto-annotated: from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
# Auto-annotated: from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
# Auto-annotated: from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
# Auto-annotated: from selenium import webdriver
from selenium import webdriver
# Auto-annotated: from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023
# Auto-annotated: from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
# Auto-annotated: from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
# Auto-annotated: from datetime import datetime, timedelta
from datetime import datetime, timedelta
# Auto-annotated: imports pandas
import pandas as pd
# Auto-annotated: imports xlsxwriter
import xlsxwriter
# Auto-annotated: imports time
import time
# Auto-annotated: from datetime import datetime, timedelta
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
# Auto-annotated: for i in range(0, len(area1), 1)
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
