import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go

stocks = px.data.stocks()
print(stocks.head())  # 顯示前5行數據

stock = px.data.stocks(indexed=True) - 1  # 將原始資料減掉1
print(stock.head())  # 顯示前5行數據


fig=px.area(
    stock,
    facet_col="company", #顯示不同元素的數據
    facet_col_wrap=2 #每列顯示的圖形數量
    )



fig.show()
