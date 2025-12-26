# 如何生成一個datetime時間對象
import plotly.graph_objects as go
from datetime import datetime

datetime(year=2013, month=10, day=10) 
# 繪製的4份數據
open_data = [133.0, 133.3, 133.5, 133.0, 134.1]
high_data = [133.1, 133.3, 133.6, 133.2, 134.8]
low_data = [132.7, 132.7, 132.8, 132.6, 132.8]
close_data = [133.0, 132.9, 133.3, 133.1, 133.1]

# 繪圖的5個日期：指定年、月、日
dates = [datetime(year=2019, month=10, day=10),
         datetime(year=2019, month=11, day=10),
         datetime(year=2019, month=12, day=10),
         datetime(year=2020, month=1, day=10),
         datetime(year=2020, month=2, day=10)]


fig=go.Figure(data=go.Ohlc(
    x=dates,
    open=open_data,
    high=high_data,
    low=low_data,
    close=close_data,
    ))

fig.show()