# 註解（自動）：匯入 pandas
import pandas as pd
# 註解（自動）：匯入 numpy
import numpy as np
# 註解（自動）：匯入 plotly_express
import plotly_express as px
# 註解（自動）：匯入 plotly.graph_objects
import plotly.graph_objects as go

stocks = px.data.stocks()
print(stocks.head())  # 顯示前5行數據

stock = px.data.stocks(indexed=True) - 1  # 將原始資料減掉1
print(stock.head())  # 顯示前5行數據

# 繪製FB股票走勢

'''
fig = px.line(
    stocks,
    x='date',
    y='FB'
)

fig=go.Figure(
    [go.Scatter(x=stocks['date'],y=stocks['FB'])]
    )
'''
fig = px.bar(
  stock,  # 數據
  x=stock.index,  # x軸 
  y="GOOG"  # y軸
)



fig.update_layout(title={
    'text':'Facebook股票走勢',
    'x':0.52,
    'y':0.96,
    'xanchor':'center',
    'yanchor':'top'
})

fig.show()
