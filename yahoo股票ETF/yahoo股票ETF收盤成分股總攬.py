# 註解（自動）：匯入 yfinance
import yfinance as yf   
# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：匯入 matplotlib.pyplot
import matplotlib.pyplot as plt


x=["0050.TW","1101.TW","1216.TW"]
df=yf.download(x,start='2020-1-1',end='2024-5-9')
df=df[['Close']]
df=df.rename(columns={'Close':'0050'})
print(df)

df.to_csv('out.csv', index=False)
'''
df.plot(kind='line',figsize=(12,6),y=['Close'])
plt.show()
'''
