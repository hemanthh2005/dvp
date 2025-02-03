import pandas as pd
import plotly.express as plt
import plotly.io as pio

df=pd.read_csv('dataset6.csv')
fig=plt.line(df,x='timestamp',y='temperature',title='Temperature Overtime',markers='o',labels={'timestamp':'Timestamp','temperature':'Temperature(c)'})

fig.update_layout(title_text='Temperature OverTime',xaxis_title='Timestamp',yaxis_title='Temperature(c)',hovermode='x unified')

fig.update_traces(mode='lines+markers',line=dict(color='blue',width=2),marker=dict(color='red',size=8,line=dict(color='black',width=2)))

fig.update_xaxes(tickangle=45)

pio.renderers.default='browser'

fig.show()