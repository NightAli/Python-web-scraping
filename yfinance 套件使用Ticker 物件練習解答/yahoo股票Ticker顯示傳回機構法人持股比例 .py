# Auto-annotated: imports yfinance
import yfinance as yf   
# Auto-annotated: imports pandas
import pandas as pd
# Auto-annotated: imports matplotlib.pyplot
import matplotlib.pyplot as plt


    
TSLA=yf.Ticker('TSLA')      # 特斯拉  
print(TSLA.get_institutional_holders())	# 顯示傳回機構法人持股比例 
