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
browser.get("https://www.mobile01.com/topicdetail.php?f=294&t=6959162")
time.sleep(3)

html_source=browser.page_source  #取得網頁原始碼
elem=browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div/label/input") #抓顯示更多按鈕,方法二
elem.click()
browser.close()
