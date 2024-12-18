import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib.dates as mdates

df = pd.read_csv(
    'files/btc-market-price.csv',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
)
# print(df.head())

eth = pd.read_csv('files/eth-price.csv', parse_dates=True, index_col=0)
prices = pd.DataFrame(index=df.index)
prices.head()
prices['Bitcoin'] = df['Price']
prices['Ether'] = eth['Value']
print(prices.head())

# prices.plot(figsize=(12, 6))#nusirodom dydi
# prices.loc['2017-12-01':'2018-01-01'].plot(figsize=(12, 6))#prisizoominam
# plt.show()

# print(prices['Ether'].isna().values.any())
# print(prices.loc[prices['Ether'].isna()])


#=======================skylės========================================
# prices.loc['2017-12-06': '2017-12-12'].fillna(method='ffill') #netinkami budai
# prices.loc['2017-12-06': '2017-12-12'].ffill(inplace=True)#netinkami budai

# prices.loc['2017-12-06': '2017-12-12', :] = prices.loc['2017-12-06': '2017-12-12', :].ffill()
# prices.plot(figsize=(12, 6))#prisizoominam
# plt.show()



#=======================extremumai====================================
df = pd.read_csv(
    'files/btc-eth-prices-outliers.csv',
    index_col=0,
    parse_dates=True
)

# print(df.head())
# df.plot()
# plt.show()

# df['2017-12-27':'2017-12-28'].plot()
# plt.show()

df.loc['2017-12-06': '2017-12-12', :] = df.loc['2017-12-06': '2017-12-12', :].ffill()
fdf = df.drop(pd.to_datetime(['2017-12-28']))
fdf = fdf.drop(pd.to_datetime(['2018-03-04']))
# fdf.plot()
# plt.show()


#===================== kainu pasiskirstymas==========================

# fdf.plot(kind='hist', y='Ether',bins=10)# bins - stulpeliu skaicius i kiek daliu sugrupuojama duomenys
# fdf.plot(kind='hist', y='Bitcoin',bins=10)# bins - stulpeliu skaicius i kiek daliu sugrupuojama duomenys
# plt.show()

# fig, axes = plt.subplots(1,2,figsize=(14, 6))
# fdf['Ether'].plot(kind='hist',bins=150, ax=axes[0],title="Ethereum")
# fdf['Bitcoin'].plot(kind='hist',bins=150, ax=axes[1],title="Bitcoin")
# plt.show()


##################### Su KDE kreive #####################
# sns.displot(fdf['Ether'],kde=True)
# sns.displot(fdf['Ether'],kde=True, height=7,aspect=2)
# sns.displot(fdf['Ether'],kde=True, height=7,aspect=2, binwidth=10)#galima ir patiems nurodyti zingsni
# sns.displot(fdf['Ether'],kde=True, height=7,aspect=2, bins=10)#galima ir patiems nurodyti stulpeliu kieki
# plt.show()


#==== galime kdeplot ir rugplot naudoti kartu, arba atskirai ====
# sns.kdeplot(fdf['Ether'],shade=True,cut=0)
# # plt.show()
# sns.rugplot(fdf['Ether'])
# plt.show()


#================= rodo iprastai ir cummulative ====================
#pip install scipy

#cumulative
# False → "How often does this price occur?" (real frequency)
# True → "How many times has the price been this or lower?" (cumulative). (Y stulpelis rodo 365 reiksmes, kiek irasu
# fig, ax = plt.subplots(figsize=(15, 7))
# sns.histplot(fdf['Bitcoin'], cumulative=False, kde=True, kde_kws={'cumulative': True})
# sns.histplot(fdf['Bitcoin'], cumulative=True, kde=True, kde_kws={'cumulative': True})
# plt.show()

#============== BI-varieties distributions ======================
# sns.jointplot(x="Bitcoin", y='Ether',data=fdf, height=7)
# plt.show()



# fdf.reset_index(inplace=True)

# fig = px.scatter(fdf, x='Bitcoin', y='Ether', hover_data={'Timestamp': True})
# fig.show()
# alternatyva su stulpeliais

# fig = px.scatter(fdf,
#                  x='Bitcoin',
#                  y='Ether',
#                  marginal_x="histogram",   # Adds histogram on x-axis
#                  marginal_y="histogram",   # Adds histogram on y-axis
#                  hover_data={'Timestamp': True},
#                  height=700, width=700)
# fig.show()


# procentine priklausomybe. matome, kad renkasi apie centra, reiskias procentaliai kyla panasiai
# fdf['BTC_Percent_Change'] = fdf['Bitcoin'].pct_change() * 100
# fdf['ETH_Percent_Change'] = fdf['Ether'].pct_change() * 100
# fig = px.scatter(fdf,
#                  x='BTC_Percent_Change',
#                  y='ETH_Percent_Change',
#                  title="Dependency of Bitcoin and Ethereum Price Increases by Percent",
#                  labels={'BTC_Percent_Change': 'Bitcoin % Change', 'ETH_Percent_Change': 'Ethereum % Change'},
#                  height=700)
# fig.show()

#BTC ir ETH KAINU koreliacija
# fig, ax = plt.subplots(figsize=(12, 5))
# sns.regplot(x="Bitcoin", y="Ether", data=fdf, ax=ax)
# plt.show()


# stipri koreliacija
timestamps = pd.date_range(start='2023-01-01', periods=100, freq='D')
# bitcoin_strong = np.linspace(20000, 40000, 100) + np.random.normal(0, 1000, 100)
# ethereum_strong = np.linspace(1500, 3000, 100) + np.random.normal(0, 100, 100)
# df_strong_corr = pd.DataFrame({
#     'Timestamp': timestamps,
#     'Bitcoin': bitcoin_strong,
#     'Ether': ethereum_strong
# })
# sns.regplot(x="Bitcoin", y="Ether", data=df_strong_corr, ax=ax)
# plt.show()


#silpna koreliacija
# bitcoin_weak = np.random.normal(20000, 5000, 100)
# ethereum_weak = np.random.normal(1500, 500, 100)
#
# df_weak_corr = pd.DataFrame({
#     'Timestamp': timestamps,
#     'Bitcoin': bitcoin_weak,
#     'Ether': ethereum_weak
# })
# sns.regplot(x="Bitcoin", y="Ether", data=df_weak_corr, ax=ax)
# plt.show()




#stiprejanti koreliacija
# timestamps = pd.date_range(start='2023-01-01', periods=10, freq='D')
# # Bitcoin prices showing random movements
# bitcoin_start = [21000, 21300, 20800, 20700, 21050, 21400, 21500, 21350, 21600, 21450]
# # Ethereum starts weakly correlated with Bitcoin, but gradually becomes more correlated
# ethereum_start = [1600, 1620, 1640, 1580, 1605, 1625, 1640, 1650, 1645, 1635]
# # Gradually increase correlation by making Ethereum's price more dependent on Bitcoin's
# for i in range(1, 10):
#     ethereum_start[i] += (bitcoin_start[i] - 21000) * 0.01  # Increasing dependency on Bitcoin
# df_stronger_corr = pd.DataFrame({
#     'Timestamp': timestamps,
#     'Bitcoin': bitcoin_start,
#     'Ether': ethereum_start
# })
# sns.regplot(x="Bitcoin", y="Ether", data=df_stronger_corr, ax=ax)
# plt.show()





#=============== procentinio kainu kilimo priklausomybe =================

# fdf['Bitcoin_pct_change'] = fdf['Bitcoin'].pct_change() * 100
# fdf['Ether_pct_change'] = fdf['Ether'].pct_change() * 100
#
# # Calculate the correlation between the percentage changes
# correlation = fdf[['Bitcoin_pct_change', 'Ether_pct_change']].corr().iloc[0, 1]
# print(f"Correlation between Bitcoin and Ether growths: {correlation}")
#
# # Plot the percentage growths
# plt.plot(fdf.index, fdf['Bitcoin_pct_change'], label='Bitcoin % Growth', marker='o')
# plt.plot(fdf.index, fdf['Ether_pct_change'], label='Ether % Growth', marker='x')
# plt.xlabel('Timestamp')
# plt.ylabel('% Growth')
# plt.title('Bitcoin vs Ether Percentage Growth Over Time')
# plt.legend()
# plt.grid(True)
# plt.show()





#========================IMTYS===============================
# * Range
# * Variance and Standard Deviation
# * IQR

# data = [1,1,2,1,100]
# mean = np.mean(data)
# std_deviation = np.std(data)
# variance = np.var(data)
# print(f"Data: {data}")
# print(f"Mean: {mean}") # vidurkis
# print(f"Standard Deviation: {std_deviation}") # kuo didesnis tuo nestabilesni pokyciai, labiau issibarste,
# print(f"Variance: {variance}")#tiesiog kvadratas




# grazu, rodo visas datas
# ax = fdf[['Bitcoin', 'Ether']].plot(kind='bar', figsize=(10, 6), width=0.8)
# ax.set_title('Bitcoin and Ether Prices')
# ax.set_xlabel('Date')
# ax.set_ylabel('Price')
# plt.show()


#sugrupuoja pasavaiciui pagal vidurkius savaites, uzmeta eth ant btc
# df_weekly = fdf.resample('W').mean()
# ax = df_weekly[['Bitcoin', 'Ether']].plot(kind='bar', figsize=(10, 6), width=0.8, position=1)
# ax.set_title('Weekly Average Bitcoin and Ether Prices')
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# ax.set_xlabel('Date')
# ax.set_ylabel('Price')
# plt.xticks(rotation=45)
# plt.show()




#sukisa overlap
# df_weekly = fdf.resample('W').mean()
# fig, ax = plt.subplots(figsize=(10, 6))
# df_weekly['Bitcoin'].plot(kind='bar', ax=ax, width=0.8,  color='blue', alpha=0.7)
# df_weekly['Ether'].plot(kind='bar', ax=ax, width=0.8, color='orange', alpha=0.7)
# ax.set_title('Weekly Average Bitcoin and Ether Prices (Overlapping)')
# ax.set_xlabel('Date')
# ax.set_ylabel('Price')
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.xticks(rotation=45)
# plt.show()



#sutvarko  datas apacioj
df_weekly = fdf.resample('W').mean()
fig, ax = plt.subplots(figsize=(10, 6))
df_weekly['Bitcoin'].plot(kind='bar', ax=ax, width=0.8, color='blue', alpha=0.7)
df_weekly['Ether'].plot(kind='bar', ax=ax, width=0.8, color='orange', alpha=0.7)
ax.set_title('Weekly Average Bitcoin and Ether Prices (Overlapping)')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
# Format the x-axis labels to display every 4th date
ticks = range(0, len(df_weekly), 4)  # Select every 4th tick position
ax.set_xticks(ticks)  # Apply tick positions
ax.set_xticklabels(df_weekly.index[ticks].strftime('%Y-%m-%d'), rotation=45)
plt.tight_layout()
plt.show()


