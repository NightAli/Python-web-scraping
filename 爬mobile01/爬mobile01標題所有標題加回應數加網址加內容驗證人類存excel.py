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
browser.get("https://www.mobile01.com/hottopics.php?id=6")
time.sleep(5)

#捲動瀏覽器
last_height=browser.execute_script("return document.body.scrollHeight") #目前視窗高度
print("舊視窗高度:",last_height)
b1=3 #紀錄按下"顯示更多"倒數次數
# Auto-annotated: while
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight*0.8);") #捲動視窗方法2
    time.sleep(3)
    new_height=browser.execute_script("return document.body.scrollHeight") #目前視窗高度
    print("新視窗高度:",new_height)
    
   
    
# Auto-annotated: if new_height == last_height
    if new_height==last_height:
        print("捲到底了")
        break
    else:
        last_height=new_height  #紀錄目前高度


df=pd.DataFrame(columns=["標題","網址","內容","回應"])  #宣告空的df

html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("div",class_="l-listTable__tr")
# Auto-annotated: for i in range(1, len(area1), 1)
for i in range(1,len(area1),1):
    title=area1[i].find("div",class_="c-listTableTd__title")
    title2=title.find("a")
    print("標題:"+title2.text)
    link1="https://www.mobile01.com/"+title2.get('href')
    print("網址:"+link1)
    
    
    browser2=webdriver.Chrome(options=chrome_options)
    browser2.get(link1)
    time.sleep(3)
# Auto-annotated: try/except/finally block
    try:
        elem=browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div/label/input") #抓驗證人類,方法二
# Auto-annotated: if elem
        if elem:
            elem.click()
            print("驗證人類...")
            time.sleep(3)
    except:
        print("繼續...")
    html_source2=browser2.page_source  #取得網頁原始碼
    soup2=BeautifulSoup(html_source2,"lxml")
    area2=soup2.find_all("article",class_="l-publishArea topic_article")
    content=area2[0].text
    print("內容:"+area2[0].text)
    browser2.close()
    
    
    rno=area1[i].find("div",class_="o-fMini")
    print("回應:"+rno.text)
    print("------------------")
    
    df.loc[i]=[title2.text,link1,content,rno.text]
    
# Auto-annotated: if i > 3
    if i>3:break  #紀錄5筆資料
browser.close()

#df.to_csv("mobile01.csv",encoding="utf_8_sig")  #存成csv
#存成excel
writer=pd.ExcelWriter("mobile01.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="mobile01")
writer.close()
