import pandas as pd
res=pd.read_csv("D:\\result.csv")
print(res)
#1)display top 3 scorers of Mathematics
s=res['Math'].sort_values(ascending=False).head(3)
print(s)

#2) add two columns total and percent
res['Total']=res['Math']+res['Science']+res['English']+res['Computer']
res['Percent']=res['Total']/4
print(res)

#3) display the names of students failing in Science
print(res[res['Science']<50].Sname)

#4) display the names of students getting distinction in Math
#5) plot line graph to compare marks
import matplotlib.pyplot as pt
pt.plot(res.Sname,res.English,label='English',marker='*')
pt.plot(res.Sname,res.Science,label='Science',marker='x')
pt.plot(res.Sname,res.Math,label='Math',marker='p')
pt.plot(res.Sname,res.Computer,label='Computer',marker='<')
pt.legend(loc=2)
pt.grid()
pt.show()
