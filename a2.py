import matplotlib.pyplot as pt
import numpy as np
x=np.array([20,67,41,76,90,43,58,70,83,64])
y=np.array([39,45,73,91,64,80,61,50,29,56])
pt.scatter(x,y)
pt.xticks(range(20,91,2))
pt.yticks(range(25,96,2))
pt.grid()
pt.show()