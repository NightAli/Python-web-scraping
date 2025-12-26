from FinMind.data import DataLoader

dl=DataLoader()
future_data=dl.taiwan_futures_daily(futures_id='TX',start_date='2020-01-01')
print(future_data)