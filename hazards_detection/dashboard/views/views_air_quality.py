import dash
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from dashboard.utils.utils import get_dataset
from dashboard.utils.utils import labels_dict
import dpd_components as dpd
import plotly.graph_objects as go



import pandas as pd

df = get_dataset()

labels = labels_dict

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

available_indicators = df.columns[2:-1]


## Variables Relationshipts

app = DjangoDash('VariablesRelationship', external_stylesheets=external_stylesheets)


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


## Variables by Date
app_dates = DjangoDash('MeasurementDates',
                 external_stylesheets=external_stylesheets)

app_dates.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='air_data_value'
            ),
        ],
            style={'width': '48%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='indicator-graphic'),
])


@app_dates.callback(
    Output('indicator-graphic', 'figure'),
    [Input('yaxis-column', 'value'), ])
def update_graph_dates(yaxis_column_name):
    
    df_by_months = pd.DataFrame(df.groupby(df['stime'].dt.strftime('%B'))[
                                yaxis_column_name].mean().sort_values(ascending=False)).reset_index()

    print(df_by_months)

    fig = px.scatter(df_by_months, x='stime', y=yaxis_column_name, labels={
                     yaxis_column_name: labels[yaxis_column_name], 'stime': '2019'})

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')


    fig.update_yaxes(title='Average ' + labels[yaxis_column_name])

    return fig


## Country
app_country = DjangoDash('CountryMap',
                       external_stylesheets=external_stylesheets)

df_country = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')

df_country['text'] = df_country['name'] + '<br>Population ' + \
    (df_country['pop']/1e6).astype(str)+' million'
limits = [(0, 2), (3, 10), (11, 20), (21, 50), (50, 3000)]
colors = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"]
cities = []
scale = 5000

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df_country[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode='USA-states',
        lon=df_sub['lon'],
        lat=df_sub['lat'],
        text=df_sub['text'],
        marker=dict(
            size=df_sub['pop']/scale,
            color=colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode='area'
        ),
        name='{0} - {1}'.format(lim[0], lim[1])))

fig.update_layout(
    title_text='US city populations<br>',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(217, 217, 217)',
    )
)

app_country.layout = html.Div([
    dcc.Graph(id='indicator-graphic', figure=fig),
])
