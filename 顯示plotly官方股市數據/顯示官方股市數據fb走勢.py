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

# 繪製FB股票走勢

fig = px.line(
    stocks,
    x='date',
    y='FB'
)

fig.update_layout(title={
    'text':'Facebook股票走勢',
    'x':0.52,
    'y':0.96,
    'xanchor':'center',
    'yanchor':'top'
})

fig.show()
