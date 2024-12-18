import numpy as np
import pandas as pd

#================ reiksmiu nan ir inf tvarkymas =========================
#================ ===========numpy============= =========================
# a = np.array([1,2,3,np.nan, 4])
# print(a.sum()) #gausim nan
# print(np.isnan(a)) #gausim true false masyva
# print(np.nansum(a)) #sumuos skaicius
# print( a[~np.isnan(a)].sum())#sumuos skaicius net jei yra np.nan
# print( a[~np.isinf(a)].sum())#sumuos skaicius net jei yra np.inf
# print("---------------------")
#================ ===========Pandas============ =========================
#================ ===========series============ =========================

# sr = pd.Series([1,2,3,np.nan, None, 4])
# print(sr.count()) #skaiciuoja validzias reiksmes
# print(len(sr)) # pasako series ilgi
# print(sr.sum())
# print(sr.mean())
# print(pd.notna(sr))
# print(pd.notnull(sr))
#
# print(sr[pd.notna(sr)])
# print("------------")
# sr_non_na = sr.dropna()
# print(sr_non_na)
# print(sr)


#================ ===========DataFrame============ =========================

df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110]
})
print(df)
# print("------------")
# print(df.dropna())# any yea default
# print(df.dropna(how="any"))#dropina eilutes jei juose yra bent vienas nan
# print(df.dropna(how="all"))#dropina eilutes jei juose NERA nei vienos normalios reiksmes
# print(df.dropna(thresh=3))# tresh nurodo kiek minimaliai turi buti geru reiksmiu
# print("------------")
# print(df.fillna(0))#uzpildo nuliais (ar kita paruoda reiksme)
# print(df.loc[0].mean())

#pvz kaip nan reiksmes pakeisti eiluciu vidurkiais, koreguojam originalu dataframe
# for i in range(len(df)):
#     row = df.iloc[i]
#     df.iloc[i] = row.fillna(row.mean())
# print(df)
# print(df.ffill())
# print(df.bfill())
# print(df.ffill(axis=1))
# print(df.bfill(axis=1))
