import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# step by step
# df = pd.read_csv('files/btc-market-price.csv', header=None)
# pd.set_option('display.max_rows', None)
# df.columns = ['Date(UTC)','price']
# df['Date(UTC)'] = pd.to_datetime(df['Date(UTC)'])
# df.set_index('Date(UTC)',inplace=True)
# print(df.loc['2017-12-01':'2018-01-01'])


# su viena eilute
# btc = pd.read_csv(
#     'files/btc-market-price.csv',
#     header=None,
#     names=['Date(UTC)', 'price'],
#     index_col=0,
#     parse_dates=True
# )
#
# pd.set_option('display.max_rows', None)

# print(btc.head())
# btc.plot()
# plt.show()


# eth = pd.read_csv("files/eth-price.csv",parse_dates=True, index_col=0)
# print(eth.head())
#
# eth = pd.read_csv("files/eth-price.csv")
# print(pd.to_datetime(eth['UnixTimeStamp']))
# btc.rename(columns={'price':'BTCPrice'},inplace=True)
#
# #Kaip left join
# btc['ETHprice'] = eth['Value']
# btc['BTCPrice'] = btc['BTCPrice'].round(2)
# print(btc)

# kaip full outer join
# merged = pd.merge(btc, eth, on='Date(UTC)', how='outer', suffixes=('_btc', '_eth'))
# print(merged)

# btc.plot()
# btc.loc["2017-12-01":"2017-12-20"].plot()
# plt.show()

