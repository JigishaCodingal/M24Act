import matplotlib.pyplot as pt
names=['Riya','Somi','Viraj','Bony','Mesha','Kiti']
first=[57,36,90,82,78,58]
second=[83,63,97,52,91,70]
pt.plot(names,first,marker='p',markersize=7,markeredgecolor='r',color='g',linewidth=3,linestyle='dotted',label='First term')
pt.plot(names,second,marker='o',markersize=7,markeredgecolor='b',color='y',linewidth=3,linestyle='dashed',label='Second term')
pt.xlabel("Student name")
pt.ylabel("Student mark")
pt.title("Result")
pt.grid()
pt.legend()
pt.xticks(['Riya','Somi','Viraj','Bony','Mesha','Kiti'])
pt.yticks([35,40,45,50,55,60,65,70,75,80,85,90])

pt.show()