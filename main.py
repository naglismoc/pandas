import pandas as pd
import matplotlib.pyplot as plt

# dFrame = pd.DataFrame()
# print((dFrame))
# numbers = [1,5,10,12,1,4,16]
# letters = ['a','b','c','d','e','f','g']
#
# dFrame['skaiciai'] = numbers
# dFrame['raides'] = letters
# print(dFrame)
#
# data = {
#     'vardas':['Jonas','Petras','Anzelmas'],
#     'pavarde':['Jonaitis','Petrikas','Volfenshouveris'],
# }
# print("--------------")
# df = pd.DataFrame(data)
# print(df['vardas'])
# print(df.values[1])
# print("--------------")
#
# print(dFrame['skaiciai'].value_counts())
# print("--------------")
# print(df.loc[2])
# print("--------------")
# print(dFrame.loc[::2])
# print("--------------")
#
# print(dFrame.loc[1:5,'raides'])
# print(dFrame.loc[1:7:2,['raides','skaiciai'] ])
# print(dFrame.iloc[1:5,1]) #cia iloc, ne loc. su juo galima stulpelius imti pagal indeksą
#
# print("--------------")

# dFrame.plot()
# plt.ylabel("beprasmiai skaiciai")
# plt.show()

# data = {
#     'grades':[8,8,7,6,3,5,4,8,9,10,7,6],
#     'months':[1,2,3,4,5,6,7,8,9,10,11,12]
# }
#
# ivertinimai = pd.DataFrame(data)
# ivertinimai.plot(y='grades',x='months')
# plt.show()

# file_name = "NYPD2.csv"
# dframe = pd.read_csv(file_name, sep=',')
# dframe['OCCUR_DATE'] = pd.to_datetime(dframe['OCCUR_DATE'],format="%m/%d/%Y")#d/m/y  m/d/y y/m/d
# dframe['OCCUR_TIME'] = pd.to_datetime(dframe['OCCUR_TIME'],format="%H:%M:%S").dt.time #d/m/y  m/d/y y/m/d
# print(dframe.loc[::,['OCCUR_DATE','OCCUR_TIME']])
# alternatyva, sukuriant nauja stulpeli
# dframe['DATE'] = (pd.to_datetime(dframe['OCCUR_DATE'],format="%m/%d/%Y").astype(str) + " " +
#                   pd.to_datetime(dframe['OCCUR_TIME'],format="%H:%M:%S").dt.time.astype(str))
# print(dframe.loc[::,['DATE']])
# print("------------------")
# print(dframe.info())
# print(dframe.head())
# print(dframe.tail())
# dframe.plot(y ='PRECINCT', x = 'JURISDICTION_CODE')
# plt.show()

# print("------------------")
#
# for colName in dframe:
#     print(colName)
#
# for cell in dframe['DATE']:
#     print(cell)

# .iterrows(): Returns an index and a Series object for each row.
# .itertuples(): Returns a named tuple for each row (faster and more memory-efficient).

# for _, row in dframe[["OCCUR_DATE", "OCCUR_TIME"]].iterrows():
#     print(row["OCCUR_DATE"], row["OCCUR_TIME"])

# for row in dframe[["OCCUR_DATE", "OCCUR_TIME"]].itertuples(index=False): #greiciau
#     print(row.OCCUR_DATE, row.OCCUR_TIME)

# dframe = pd.read_csv('auto.csv', sep='|', on_bad_lines='skip')
# # print(dframe.columns.tolist())
# # print(dframe['price'])
# print(len(dframe))
# expencive_cars = dframe[(pd.to_numeric(dframe['price'], errors='coerce') >= 500) |
#                         (dframe['gamintojas'] == 'Volvo')]
# print(len(expencive_cars))
#
# min_val = dframe["price"].min()
# max_val = dframe["price"].max()
# print(min_val, max_val)


data = [
    ['Jonas','39001125478',28],#0
    ['Petras','39001125479',31],#1
    ['Kazys','39001125477',24],#2
    ['Leonidas','39001123478',26],#3
    ['Vilius','39001125148',28],#4
]


dframe = pd.DataFrame(data, columns=['vardas','asmens kodas','amzius'])
dframe['id'] = [1,2,6,40,45]
print(dframe)
print("-------")
dframe.set_index('id',inplace=True) # jei kalbam apie duomenis is DB tai turime primary key
print(dframe)
print(dframe.loc[6]) # where id = 6
print(dframe.iloc[2]) # masyve esantis elementas 3cioje pozicijoje
dframe.drop('asmens kodas', axis=1,inplace=True)
print(dframe)
dframe.drop(40,axis=0, inplace=True)
print(dframe)

dframe.loc[2] = ['PETRAS',24] #Updeitinam visa eilute
print(dframe)
dframe.loc[2,'vardas'] = 'Petras' #keiciu viena reiksme
print(dframe)


