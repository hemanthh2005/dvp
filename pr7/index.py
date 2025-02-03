import plotly.express as px
import numpy as np
import pandas as pd
import json
import plotly.io as pio

pio.renderers.default="browser"

india_states=json.load(open('states_india.geojson','r'))



df=pd.read_csv('List of states_India.csv')

state_id_map={}

df.info()

for x in india_states['features']:
    x['id']=x['properties']['state_code']
    state_id_map[x['properties']['st_nm']]=x['id']

print(df.head())
print(state_id_map)

df=pd.read_csv('State_Dataset.csv')

df['DensityScale']=np.log10(df['Density [a]'])

fig=px.choropleth(df, locations='id',
                      geojson=india_states,
                      color='DensityScale',
                      hover_name='State or Union Territory',
                      hover_data=['Density [a]'])

fig.update_geos(fitbounds='locations', visible=False)
fig.update_layout(title_text='Indian Population Density')
fig.show()


