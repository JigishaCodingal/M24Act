import pandas as pd
df=pd.DataFrame([[4,9,1,2,6,2],[7,2,1,6,7,5],[4,0,2,5,1,8],[5,9,1,2,2,4],[3,9,2,6,6,1]],['a','b','c','d','e'],['n1','n2','n3','n4','n5','n6'])
print(df)
print(df.quantile([0.25,0.5,0.75]))
import matplotlib.pyplot as pt
df.boxplot()
pt.show()