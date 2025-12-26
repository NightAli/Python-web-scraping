# Auto-annotated: imports yfinance
import yfinance as yf   
# Auto-annotated: imports pandas
import pandas as pd
# Auto-annotated: imports matplotlib.pyplot
import matplotlib.pyplot as plt


x=["0050.TW"]
df=yf.download(x,start='2020-1-1',end='2024-5-9')
print(df)

'''
df.plot(kind='line',figsize=(12,6),y=['Close'])
plt.show()
'''
