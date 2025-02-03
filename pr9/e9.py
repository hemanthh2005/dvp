import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb


df=pd.read_csv('e9.1.csv')
plt.figure(figsize=(12,8))

sb.lineplot(x='Date',y='Total cases',hue='Country',marker='o',data=df)
plt.title('Global COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.show()

top_countries=df.groupby('Country')['Total cases'].max().sort_values(ascending=False).head(5)
plt.figure(figsize=(5,5))
sb.barplot(x=top_countries.values,y=top_countries.index,palette='viridis')
plt.show()

df['Mortality Rate']=(df['Total Deaths']/df['Total cases']*100)
plt.figure(figsize=(12, 6))
sb.lineplot(x='Date',y='Mortality Rate',hue='Country',marker='o',data=df)
plt.xlabel('Date')
plt.show()

df['Recovery Rate']=(df['Total Recovered'])/df['Total cases']*100
plt.figure(figsize=(12,6))
sb.lineplot(x='Date',y='Recovery Rate',hue='Country',marker='o',data=df)
plt.show()