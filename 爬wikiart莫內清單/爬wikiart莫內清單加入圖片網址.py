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
# Auto-annotated: imports requests
import requests



#設定瀏覽器驅動程式與爬蟲網址
chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://www.wikiart.org/en/claude-monet/all-works/text-list")
time.sleep(5)


#宣告變數值
df=pd.DataFrame(columns=["作品名稱","作品年份","作品網址","圖片網址"])  #宣告空的df
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
    link1="https://www.wikiart.org"+area1[i].find("a").get('href')

    #爬圖片網址
    browser.get(link1)
    time.sleep(2)
    html_source2=browser.page_source  #取得網頁原始碼
    soup2=BeautifulSoup(html_source2,"lxml") 
    imgbox1=soup2.find("div",class_="wiki-layout-artist-image-wrapper btn-overlay-wrapper-artwork ng-scope")    #抓圖片區塊
    imglink1=imglink1=imgbox1.find("img").get('src') #同imgbox1.find("img")['src']

# Auto-annotated: if i > 10
    if i>10:break
    
    print("作品名稱:",name1)
    print("作品年份:",year1)
    print("作品網址:",link1)
    print("圖片網址:",imglink1)
    print("------------------")

    df.loc[x]=[name1,year1,link1,imglink1]  #紀錄存到pandas
    x=x+1

    #處理圖片連結與檔名
    src=imglink1
    src=src.split("!")[0] #選擇高解析圖片網址
    print(src)
    imgname=src.split("/")[5] #選擇作品名稱

    #將圖片下載存檔
    img1=requests.get(src)  #使用requests.get取得圖片資訊
    f=open(f'download/{imgname}','wb') #將圖片開啟成為二進位格式
    f.write(img1.content)
    f.close()
    

browser.close()


#儲存成檔案
#df.to_csv("wikiart.csv",encoding="utf_8_sig")  #存成csv
#存成excel
writer=pd.ExcelWriter("wikiart.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="mobile01")
writer.close()
