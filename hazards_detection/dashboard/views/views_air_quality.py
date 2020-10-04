import dash
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from dashboard.utils.utils import get_dataset
from dashboard.utils.utils import labels_dict

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

df = get_dataset()

labels = labels_dict

available_indicators = df.columns[2:-1]

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='air_data_value'
            ),
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='RH'
            ),
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),])
def update_graph(xaxis_column_name, yaxis_column_name):
    
    fig = px.scatter(x=df[xaxis_column_name],
                     y=df[yaxis_column_name], color=df['PM High'])

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=labels[xaxis_column_name])

    fig.update_yaxes(title=labels[yaxis_column_name])

    

    return fig
