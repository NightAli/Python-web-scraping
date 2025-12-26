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
browser.get("https://www.mobile01.com/topicdetail.php?f=294&t=6959162")
time.sleep(3)

html_source=browser.page_source  #取得網頁原始碼
elem=browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div/label/input") #抓顯示更多按鈕,方法二
elem.click()
browser.close()
