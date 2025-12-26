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


fig=px.area(
    stock,
    facet_col="company", #顯示不同元素的數據
    facet_col_wrap=2 #每列顯示的圖形數量
    )



fig.show()
