#pair plot
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as pt
df=sb.load_dataset('iris')
sb.set_style('ticks')
sb.pairplot(df,hue='species',diag_kind='kde',kind='scatter')
pt.show()