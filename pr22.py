import matplotlib.pyplot as pt
names=['Viya','Dwij','Kitty','Sini','Tark','Yom']
E1=[54,97,82,68,70,38]
E2=[50,100,72,86,58,50]
E3=[68,90,79,75,86,65]
pt.bar(names,E1,width=0.8,label="Exam 1",color='c')
pt.bar(names,E2,width=0.4,label="Exam 2",color='y')
pt.bar(names,E3,width=0.2,label="Exam 3",color='m')
pt.legend()
pt.show()