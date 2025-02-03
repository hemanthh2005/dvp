import dash
from dash import dcc,html
from dash.dependencies import Input,Output
import plotly.express as plt
import pandas as pd
from matplotlib.pyplot import figure

df=pd.read_csv('Pgm8_dataset.csv')

app=dash.Dash(__name__)

app.layout=html.Div([
    html.H1('Interactive Dashboard'),

    html.Label('Select categorical Dropdown'),
        dcc.Dropdown(
        id='category-dropdown',
        options=df['Place'].unique(),
        value="BSE"),

    html.Label("Select a range of numeric values:"),
        dcc.Slider(
        id='Slider',
        min=df['Day'].min(),
        max=df['Day'].max(),
        step=1,
        value=df['Day'].min()
        ),

        dcc.Graph(id='line-plot'),

        dcc.Graph(id='bar-chart'),


    ])

@app.callback(
    [Output('line-plot','figure'),
    Output('bar-chart','figure')],

    [Input('category-dropdown','value'),
     Input('Slider','value')]
)

def update(selected_category,selected_range):
    filtered_df=df[df['Place'] == selected_category]
    filtered_df_bar=df[df['Day'] == selected_range]

    line_fig=plt.line(filtered_df,x='Date',y='Open',color='Symbol',title=f"line Plot - {selected_category}")

    bar_fig=plt.bar(filtered_df_bar,x='Date',y='Open',color='Symbol',title=f"Bar Chart - {selected_range}")

    return line_fig,bar_fig

if __name__=='__main__':
    app.run_server(debug=True)