# 註解（自動）：匯入 plotly.graph_objects
import plotly.graph_objects as go
# 註解（自動）：匯入 pandas
import pandas as pd
df =  pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
fig = go.Figure(data=go.Ohlc(x=df['Date'],open=df['AAPL.Open'],high=df['AAPL.High'],low=df['AAPL.Low'],close=df['AAPL.Close']))
fig.show(renderer="browser")
