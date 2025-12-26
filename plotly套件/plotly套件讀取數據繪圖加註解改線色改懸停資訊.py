# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：匯入 numpy
import numpy as np
# 註解（自動）：匯入 plotly_express
import plotly_express as px
# 註解（自動）：匯入 plotly.graph_objects
import plotly.graph_objects as go


# 讀取線上的csv文件

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
print(df.head())  # 顯示前5行數據
print(df.shape)  # 顯示資料量矩陣
print(df.columns)  # 顯示所有欄位名稱

hovertext=[] #添加懸停資訊

# 註解（自動）：對 i  在 range(len(df['AAPL.Open'])) 中迭代
for i in range(len(df['AAPL.Open'])):
    hovertext.append('開盤:'+str(df['AAPL.Open'][i])+'<br>'+'收盤:'+str(df['AAPL.Close'][i])+'<br>'+'最高:'+str(df['AAPL.High'][i])+'<br>'+'最低:'+str(df['AAPL.Low'][i]))



fig=go.Figure(data=go.Ohlc(
    x=df['Date'],
    open=df['AAPL.Open'],
    high=df['AAPL.High'],
    low=df['AAPL.Low'],
    close=df['AAPL.Close'],
    increasing_line_color='#ff0000',decreasing_line_color='#00ff00',
    text=hovertext,
    hoverinfo='text'
    ))


fig.update_layout(
    title="蘋果公司股票走勢圖",  # 標題
    yaxis_title="股票價格",  # y軸名稱
    shapes = [dict(  # 顯示 ㄒ形狀的位置和線寬等資訊
        x0='2015-06-01', x1='2016-05-13',  # x的取值
        y0=0, y1=1,  # y的取值
        xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(   #  備註信息
        x='2015-06-01', y=0.05, 
        xref='x', yref='paper',
        showarrow=False, 
        xanchor='left', 
        text='下降階段')]
)


fig.show()
