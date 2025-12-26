# Auto-annotated: imports matplotlib.pyplot
import matplotlib.pyplot as plt
# Auto-annotated: imports yfinance
import yfinance as yf
# Auto-annotated: imports numpy
import numpy as np

# 使用中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

stock_id = '2330.TW'
ohlcv = yf.Ticker(stock_id).history(period='max')

x = ohlcv.tail(120).index.astype(str)
y = ohlcv.tail(120)

# Auto-annotated: function ma(n)
def ma(n):
    return ohlcv.Close.rolling(n).mean().tail(120)

fig,ax = plt.subplots(figsize=(23,8),dpi=80,facecolor='#414343')

ax.set_facecolor('#414343')
ax.bar(x,y.Close-y.Open*0.9995,0.6,y.Open,color=['#e27980' if x>0 else '#73d9b6' for x in y.Close-y.Open])
ax.vlines(x,y.Low,y.High,color=['#e27980' if x>0 else '#73d9b6' for x in y.Close-y.Open])
# Auto-annotated: for (n, color) in zip([5, 20, 60, 120], ['#6b90e4', '#fae239', '#93d557', '#aa57d5'])
for n,color in zip([5,20,60,120],['#6b90e4','#fae239','#93d557','#aa57d5']):
    ax.plot(x,ma(n),color=color,label=f"ma{n}")

ax2 = ax.twinx()
ax2.bar(x,y.Volume,color='#39a1fa',alpha=.2)

ax.set_title(f"{stock_id} 個股K線圖",fontsize=25,color='w',loc='left',y=1.1)
ax.set_xlabel('Date',fontsize=13,color='w')
ax.set_ylabel('Price',fontsize=13,color='w')
ax2.set_ylabel('Volume',fontsize=13,color='w')
ax.tick_params('x',labelcolor='w')
ax.tick_params('y',labelcolor='w')
ax2.tick_params('y',labelcolor='w')

ax.text(x[1],y.Close.mean(),
        f"{y.index[-1].strftime('%Y-%m-%d')}\n\n開:{y.Open[-1]}\n收:{y.Close[-1]}\n高:{y.High[-1]}\n低:{y.Low[-1]}\n量:{y.Volume[-1]}\n幅:{round(((y.Close/y.Close.shift())[-1]-1)*100,2)} %",

color='w',fontsize=18,bbox=dict(boxstyle='round',ec='#fa397708',fc='#fa397708'))

ax.legend(fontsize=12,loc='upper left')
ax.set_xticks(np.arange(0,len(x),len(x)/10))
ax.grid('-',alpha=.5)

plt.show()
