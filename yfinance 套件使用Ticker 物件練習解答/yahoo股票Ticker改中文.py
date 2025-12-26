# Auto-annotated: imports yfinance
import yfinance as yf   
# Auto-annotated: imports pandas
import pandas as pd
# Auto-annotated: imports matplotlib.pyplot
import matplotlib.pyplot as plt

#print(type(yf.Ticker))
    
tw2330=yf.Ticker("2330.TW")      # 台積電  
#print(tw2330.history(period='max')) 


df=tw2330.history(period='max').rename(columns={'Open':'開盤價','High':'最高價','Low':'最低價','Close':'收盤價'})
print(df)
