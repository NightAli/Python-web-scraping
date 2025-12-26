import yfinance as yf   
import pandas as pd
import matplotlib.pyplot as plt


    
TSLA=yf.Ticker('TSLA')      # 特斯拉  
print(TSLA.get_institutional_holders())	# 顯示傳回機構法人持股比例 