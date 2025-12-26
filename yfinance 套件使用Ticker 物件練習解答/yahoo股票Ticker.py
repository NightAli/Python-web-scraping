# 註解（自動）：匯入 yfinance
import yfinance as yf   
# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：匯入 matplotlib.pyplot
import matplotlib.pyplot as plt

#print(type(yf.Ticker))
    
tw2330=yf.Ticker("2330.TW")      # 台積電  
#print(tw2330.history(period='max')) 

