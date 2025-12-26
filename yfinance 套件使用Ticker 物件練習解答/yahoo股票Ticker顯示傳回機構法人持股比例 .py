# 註解（自動）：匯入 yfinance
import yfinance as yf   
# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：匯入 matplotlib.pyplot
import matplotlib.pyplot as plt


    
TSLA=yf.Ticker('TSLA')      # 特斯拉  
print(TSLA.get_institutional_holders())	# 顯示傳回機構法人持股比例 
