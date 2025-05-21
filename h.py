#heat map
import numpy as np
import seaborn as sb
sb.set_theme()
data=np.random.rand(10,20)
ax=sb.heatmap(data)
import matplotlib.pyplot as pt
pt.show()
