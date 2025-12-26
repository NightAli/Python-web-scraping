import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go


# 讀取線上的csv文件

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
print(df.head())  # 顯示前5行數據
print(df.shape)  # 顯示資料量矩陣
print(df.columns)  # 顯示所有欄位名稱


