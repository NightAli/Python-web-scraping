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

fig=go.Figure(data=go.Ohlc(
    x=df['Date'],
    open=df['AAPL.Open'],
    high=df['AAPL.High'],
    low=df['AAPL.Low'],
    close=df['AAPL.Close'],
    ))

fig.show()
