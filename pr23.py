import matplotlib.pyplot as pt
import numpy as np
names=['Viya','Dwij','Kitty','Sini','Tark','Yom']
E1=[54,97,82,68,70,38]
E2=[50,100,72,86,58,50]
E3=[68,90,79,75,86,65]
x=np.arange(len(E1))
pt.bar(names,E1,width=0.2,label="Exam 1",color='c')
pt.bar(x+0.2,E2,width=0.2,label="Exam 2",color='y')
pt.bar(x+0.4,E3,width=0.2,label="Exam 3",color='m')
pt.legend()
pt.show()