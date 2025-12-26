import yfinance as yf   
import pandas as pd
import matplotlib.pyplot as plt

stock_list=['0050','1101','1216','1301','1303','1326','1590','2002','2207','2603','2801','2880','2881','2882','2883','2884','2885','2886','2887','2890','2891','2892','5876','5880','2912','5871','6505','2303','2330','2379','2408','2454','3034','3661','3711','2301','2357','2382','2395','3231','4938','6669','3008','2345','2412','3045','4904','2308','2327','3037','2317']

for i in range(0,len(stock_list),1):
    stock_list[i]=stock_list[i]+".TW"
#print(stock_list)


x=stock_list
df=yf.download(x,start='2020-1-1',end='2024-5-9')
df=df[['Close']]
df=df.rename(columns={'Close':'0050'})
print(df)

df.to_csv('out.csv', index=False)


'''
df.plot(kind='line',figsize=(12,6),y=['Close'])
plt.show()
'''