import matplotlib.pyplot as pt
name=['Samhith','Gira','Vaishnav','Yusra','Aadil','Anto']
Eng=[78,56,90,61,82,76]
Phy=[92,64,87,72,92,56]
Chem=[82,70,83,69,79,68]
Bio=[95,49,98,51,70,34]
pt.plot(name,Eng,marker='p',markersize=10,markeredgecolor='y',color='r',ls='dotted',label='English')
pt.plot(name,Phy,marker='<',markersize=10,markeredgecolor='b',color='g',ls='dotted',label='Physics')
pt.plot(name,Chem,marker='*',markersize=10,markeredgecolor='c',color='y',ls='dotted',label='Chemistry')
pt.plot(name,Bio,marker='1',markersize=10,markeredgecolor='g',color='k',ls='dotted',label='Biology')
pt.xlabel('Student Names')
pt.ylabel('Student Marks')
pt.title('Result')
pt.grid()
pt.legend(loc=1)
pt.show()