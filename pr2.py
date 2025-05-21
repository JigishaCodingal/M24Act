import seaborn
import matplotlib.pyplot as pt
df=seaborn.load_dataset('tips')
seaborn.pairplot(df,hue='sex')
seaborn.pairplot(df,hue='day')
pt.show()