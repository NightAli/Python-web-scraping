# 註解（自動）：匯入 yfinance
import yfinance as yf   
# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：匯入 matplotlib.pyplot
import matplotlib.pyplot as plt
# 註解（自動）：匯入 stocklist
import stocklist #爬公開資訊ETF成分股抓表格列清單存成清單轉函式

#stock_list=['0050','1101','1216','1301','1303','1326','1590','2002','2207','2603','2801','2880','2881','2882','2883','2884','2885','2886','2887','2890','2891','2892','5876','5880','2912','5871','6505','2303','2330','2379','2408','2454','3034','3661','3711','2301','2357','2382','2395','3231','4938','6669','3008','2345','2412','3045','4904','2308','2327','3037','2317']
stock_list=stocklist.stocklist()

# 註解（自動）：對 i  在 range(0, len(stock_list), 1) 中迭代
for i in range(0,len(stock_list),1):
    stock_list[i]=stock_list[i]+".TW"
#print(stock_list)


x=stock_list
df=yf.download(x,start='2020-1-1',end='2024-5-9')
df=df[['Close']]
df=df.rename(columns={'Close':'0050'})
print(df)

df.to_csv('0050.csv', index=False)


'''
df.plot(kind='line',figsize=(12,6),y=['Close'])
plt.show()
'''
