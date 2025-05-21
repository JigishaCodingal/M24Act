import pandas as pd
import numpy as np
Res=pd.DataFrame([[39,np.nan,47],[80,85,97],[91,59,np.nan],[81,74,70],[93,np.nan,91],[100,82,97],[np.nan,55,39]],['S1','S2','S3','S4','S5','S6','S7'],['SA1','SA2','Annual'])
print(Res)
'''
print(Res.index)
print(Res.columns)
print(Res.axes)
print(Res.values)
print(Res.dtypes)
print(Res.ndim)
#print(Res.nbytes)
print(Res.shape)
print(Res.size)
print(Res.empty)
print(Res.T)
print(len(Res))
print(Res.count())
'''

print(Res.isnull())
print(Res.notnull())

