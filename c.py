import pandas as pd
import seaborn as sb
from matplotlib import pyplot as pt
df=sb.load_dataset('iris')
sb.distplot(df['petal_length'],kde=False)
pt.show()
