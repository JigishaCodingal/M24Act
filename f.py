import pandas as pd
import seaborn as sb
from matplotlib import pyplot as pt
df=sb.load_dataset('iris')
sb.jointplot(x='petal_length',y='petal_width',data=df)
pt.show()