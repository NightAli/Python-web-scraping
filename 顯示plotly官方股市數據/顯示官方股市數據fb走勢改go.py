# Auto-annotated: imports pandas
import pandas as pd
# Auto-annotated: imports numpy
import numpy as np
# Auto-annotated: imports plotly_express
import plotly_express as px
# Auto-annotated: imports plotly.graph_objects
import plotly.graph_objects as go

stocks = px.data.stocks()
print(stocks.head())  # 顯示前5行數據

# 繪製FB股票走勢

'''
fig = px.line(
    stocks,
    x='date',
    y='FB'
)
'''
fig=go.Figure(
    [go.Scatter(x=stocks['date'],y=stocks['FB'])]
    )


fig.update_layout(title={
    'text':'Facebook股票走勢',
    'x':0.52,
    'y':0.96,
    'xanchor':'center',
    'yanchor':'top'
})

fig.show()
