import matplotlib.pyplot as pt
Phy=[56,79,48,97,26]
Chem=[86,69,58,90,66]
Bio=[50,70,40,80,46]
Math=[65,37,57,72,69]
Eng=[90,59,89,63,80]
exam=['E1','E2','E3','E4','E5']
pt.plot(exam,Phy,marker='^',markersize=15,markeredgecolor='b',ls='dotted',linewidth=3,color='r')
pt.plot(exam,Chem,marker='>',markersize=15,markeredgecolor='g',ls='dashed',linewidth=3,color='b')
pt.plot(exam,Bio,marker='<',markersize=15,markeredgecolor='m',ls='dashdot',linewidth=3,color='g')
pt.plot(exam,Math,marker='+',markersize=15,markeredgecolor='y',ls='dotted',linewidth=3,color='k')
pt.plot(exam,Eng,marker='*',markersize=15,markeredgecolor='c',ls='dashed',linewidth=3,color='y')
pt.xlabel('Name of Examination')
pt.ylabel('Marks')
pt.title('Result')
pt.show()