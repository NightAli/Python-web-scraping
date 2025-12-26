import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go

stocks = px.data.stocks()
print(stocks.head())  # 顯示前5行數據
