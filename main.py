import pandas as pd
import matplotlib.pyplot as plt

dFrame = pd.DataFrame()
print((dFrame))
numbers = [1,5,10,12,1,4,16]
letters = ['a','b','c','d','e','f','g']

dFrame['skaiciai'] = numbers
dFrame['raides'] = letters
print(dFrame)

data = {
    'vardas':['Jonas','Petras','Anzelmas'],
    'pavarde':['Jonaitis','Petrikas','Volfenshouveris'],
}
print("--------------")
df = pd.DataFrame(data)
print(df['vardas'])
print(df.values[1])
print("--------------")

print(dFrame['skaiciai'].value_counts())
print("--------------")
print(df.loc[2])
print("--------------")
print(dFrame.loc[::2])
print("--------------")

print(dFrame.loc[1:5,'raides'])
print(dFrame.loc[1:7:2,['raides','skaiciai'] ])
print(dFrame.iloc[1:5,1]) #cia iloc, ne loc. su juo galima stulpelius imti pagal indeksą

print("--------------")

# dFrame.plot()
# plt.ylabel("beprasmiai skaiciai")
# plt.show()

data = {
    'grades':[8,8,7,6,3,5,4,8,9,10,7,6],
    'months':[1,2,3,4,5,6,7,8,9,10,11,12]
}

ivertinimai = pd.DataFrame(data)
ivertinimai.plot(y='grades',x='months')
plt.show()