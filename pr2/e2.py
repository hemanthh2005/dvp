import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set(style='whitegrid')
dataset=pd.read_csv('dataset2.csv')
dataset.info()
sb.relplot(x='Maths Score',y='Science Score',hue='Gender',style='Parents Degree',data=dataset)
plt.show()