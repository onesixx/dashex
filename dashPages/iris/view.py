import dash_bootstrap_components as dbc
from dash import dcc, html



sidebarPanel = dbc.Card([
    html.Div([
        dbc.Label("X variable"),
        dcc.Dropdown(id="x-variable",
                     options=[
                         {"label": col, "value": col} for col in iris.columns
                     ],
                     value="sepal length (cm)",
                     ),
    ]),
    html.Div([
        dbc.Label("Y variable"),
        dcc.Dropdown(id="y-variable",
                     options=[
                         {"label": col, "value": col} for col in iris.columns
                     ],
                     value="sepal width (cm)",
                     ),
    ]),
    html.Div(
        [
            dbc.Label("Cluster count"),
            dbc.Input(id="cluster-count", type="number", value=3),
        ]
    ),
], body=True,)
graphs = dcc.Graph(id="cluster-graph")
app.layout = dbc.Container(
    [
        html.H1("Iris k-means clustering"), html.Hr(),
        dbc.Row([
            dbc.Col(sidebarPanel, md=4),
            dbc.Col(graphs, md=8),
        ], align="center",),
    ],
    fluid=True,
)
