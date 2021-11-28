import pandas as pd
import tushare as ts

df = pd.DataFrame()
print(df)
print(ts.__version__)
ts.get_hist_data('600848') #一次性获取全部日k线数据

pro = ts.pro_api()
df = pro.daily(trade_date='20200325')
#获取20200101～20200401之间所有有交易的日期
df = pro.trade_cal(exchange='SSE', is_open='1', 
                            start_date='20200101', 
                            end_date='20200401', 
                            fields='cal_date')

print(df.head())
