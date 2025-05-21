import matplotlib.pyplot as pt
import numpy as np
x1=np.array([106,118,129,96,200,280,150,189,300,470,350])
y1=np.array([110,123,154,160,100,210,410,390,300,410,200])

x2=np.array([96,108,120,115,150,270,165,190,270,260,380])
y2=np.array([110,138,90,129,260,298,187,301,241,194,220])

pt.scatter(x1,y1,color='b',label='Group 1')
pt.scatter(x2,y2,color='m',label='Group 2')
pt.xlabel('Height')
pt.ylabel('Weight')
pt.title('Height VS Weight')
pt.legend()
pt.grid()
pt.xticks(range(90,500,50))
pt.yticks(range(90,450,50))
pt.show()
