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
import requests



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
for i in range(0,len(area1),1):
    name1=area1[i].find("a").text
    year1=area1[i].find("span").text.replace(", ","")
    link1="https://uploads2.wikiart.org/images/claude-monet/"+area1[i].find("a").text.replace(" ","-").replace(",","")+".jpg"
    if i>10:break
    
    print("作品名稱:",name1)
    print("作品年份:",year1)
    print("圖片網址:",link1)
    print("------------------")

    df.loc[x]=[name1,year1]  #紀錄存到pandas
    x=x+1

        
    #爬圖片網址
    src=link1
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
#df.to_csv("momolist.csv",encoding="utf_8_sig")  #存成csv
#存成excel
writer=pd.ExcelWriter("momolist.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="mobile01")
writer.close()
