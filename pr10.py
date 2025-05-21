import matplotlib.pyplot as pt
name=['Samhith','Gira','Vaishnav','Yusra','Aadil','Anto']
age=[14,13,18,12,13,15]
pt.plot(name,age,marker='p',markersize=10,markeredgecolor='y',color='r',ls='dotted')
pt.xlabel('Student Names')
pt.ylabel('Student age')
pt.title('Age Comparison')
pt.grid()
pt.show()