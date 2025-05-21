import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sb
#csv : comma seperated values file
'''
df=pd.DataFrame([['Samhith',15,9,95],['Jaksith',14,8,87],['Hillarion',14,8,65]],index=['S1','S2','S3'],columns=['Name','Age','Class','Percent'])
print(df)
df.to_csv('C:\\Users\\admin\\Desktop\\stu.csv')
df1=pd.read_csv("C:\\Users\\admin\Desktop\\Book1.csv")
print(df1)
'''
print(sb.get_dataset_names())
df=sb.load_dataset('penguins')
#top 10 records
df.head(10)
#bottom 10 records
df.tail(10)
#top 5 records
df.head()
