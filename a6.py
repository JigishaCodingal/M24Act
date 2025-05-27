import matplotlib.pyplot as pt

M1=[63,80,91,79,38,46,58]
M2=[75,90,99,82,40,56,62]
L=['Sankar','Tenz','Sana','Rudra','Donald','Visha','Ritz']
pt.plot(L,M1,marker='*',markersize=10,markeredgecolor='r',color='m',ls='dotted',linewidth=5)
pt.plot(L,M2,marker='p',markersize=10,markeredgecolor='g',color='y',ls='dashed',linewidth=5)
pt.xlabel("Student Name")
pt.ylabel("Student Marks")
pt.title("Result")
pt.yticks([30,40,50,60,70,80,90,100])
pt.xticks(L)
pt.grid()
pt.show()