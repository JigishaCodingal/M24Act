import matplotlib.pyplot as pt
import seaborn as sb
import pandas as pd
df=sb.load_dataset('iris')
sb.histplot(df['petal_length'],kde=False)
sb.jointplot(x='petal_length',y='petal_width',data=df)
sb.pairplot(df,hue='species',diag_kind='kde',kind='scatter',palette='husl')
sb.set_theme()
import numpy as np
data=np.random.rand(10,12)
a=sb.heatmap(data)

pt.show()