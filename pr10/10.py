import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('10.csv')

print(data.head())

print(data.describe())

print(data.isnull().sum())
# data['OrderDate']=pd.to_datetime(data['OrderDate'])
plt.figure(figsize=(12,6))
sns.lineplot(x='OrderDate',y='OrderAmount',marker='o',data=data)
plt.title('Sales trend over time')
plt.xlabel('OrderDate')
plt.ylabel('OrderAmount')
plt.show()

customer_segment=data.groupby('CustomerID').agg({'OrderAmount':'sum','OrderDate':'count'}).reset_index()
customer_segment.rename(columns={'OrderDate':'Frequency','OrderAmount':'TotalSpending'},inplace=True)

plt.figure(figsize=(12,6))
sns.scatterplot(x='Frequency',y='TotalSpending',data=customer_segment)
plt.title('Customer Segmentation')
plt.xlabel('Frequency')


plt.ylabel('TotalSpending')
plt.show()

sns.barplot(x='ProductCategory',y='OrderAmount',data=data,estimator=sum)
plt.xlabel('Product category')
plt.ylabel('Total sales')
plt.xticks(rotation=45)
plt.show()