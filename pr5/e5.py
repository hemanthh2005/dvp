import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import csv

from matplotlib.lines import lineStyles
from seaborn import lineplot

data=pd.read_csv('dataset5.csv')
sb.lineplot(x='Date',y='Open',hue='Symbol',linestyle='dashed',style='Symbol',marker='o',data=data)
plt.xlabel('Time Line')
plt.ylabel('Opening Price')
# plt.xticks(rotation=90,ha='center',fontsize=10,fontfamily='serif',fontweight='bold')
plt.show()