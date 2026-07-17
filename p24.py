import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb
df=pd.read_csv("C:\\Users\\admin\\Downloads\\Titanic.csv")
print(df)
min=df['Age'].min()
max=df['Age'].max()
bins=[0,15,30,45,60,75]
df['bin_age']=pd.cut(df['Age'],bins)
df['bin_age']=pd.cut(df['Age'],bins,['Young','Young-Adult','Middle Aged','Middle Older Age','Senior'])
df['bin_age'].value_counts().plot(kind='bar')
pt.show()