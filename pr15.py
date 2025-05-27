#Dataframe and operations on Dataframe
import pandas as pd
L1=[[3,9,1,5],[0,9,2,8],[7,2,4,6]]
L2=['x','y','z']
L3=['a','b','c','d']
df=pd.DataFrame(L1,L2,L3)
print(df)
#check if value is null
print(df.isnull())
#check if value is not null
print(df.notnull())
