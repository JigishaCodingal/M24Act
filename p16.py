#Dataframe and operations on Dataframe
import numpy as np
import pandas as pd
L1=[[3,9,np.nan,5],[np.nan,9,np.nan,8],[7,2,np.nan,6]]
L2=['x','y','z']
L3=['a','b','c','d']
df=pd.DataFrame(L1,L2,L3)
print(df)
'''
#check if value is null
print(df.isnull())
#check if value is not null
print(df.notnull())
x=df.dropna()
print(x)
x=df.dropna(axis=1)
print(x)

x=df.dropna(how='all',axis=1)
print(x)
'''
x=df.fillna('***')
print(x)
x=df.fillna({'c':'***','a':'###'})
print(x)
