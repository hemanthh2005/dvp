import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

dataset=pd.read_csv('dataset4.csv')
dataset.info()

plt.figure(figsize=(10,8))
sb.set_style('whitegrid')
sb.violinplot(data=dataset,x='EducationLevel',y='Salary')
plt.title('Salary Details',fontsize=20)
plt.xlabel('Education Level',fontsize=25)
plt.ylabel('Salary',fontsize=25)

plt.show()

plt.figure(figsize=(10,8))
plt.title('Salary Details',fontsize=20)
sb.boxplot(data=dataset,x='EducationLevel',y='Salary')
plt.legend()
plt.grid()
plt.show()