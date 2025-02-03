import matplotlib.pyplot as plt
import seaborn as sns
import csv
import pandas as pd

x = []
y = []

with open('wr2.csv', 'r') as csvfile:
    lines = csv.reader(csvfile)
    next(lines)
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))

# data=pd.read_csv('wr2.csv')
# sns.lineplot(x='Date',y='Temperature', color='g', linestyle='dashed', marker='o', label='Temperature',data=data)
plt.plot(x,y, color='g', linestyle='dashed', marker='o', label='Temperature')
plt.xticks(rotation=25)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Weather Report', fontsize=20)
plt.grid()
plt.legend()
plt.show()
