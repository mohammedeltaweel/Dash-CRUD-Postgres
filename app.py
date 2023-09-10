import dash 
from dash import Dash, html, dcc, Input, Output, State, callback
import dash_table
import pandas as pd
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.Div(className="btn-and-input", children=[
        dcc.Input(
            id="column-name", 
            placeholder="Enter a column name",
            type="text"),
        html.Button("Add Column", className="my-btn")
    ]),
    dash_table.DataTable(),
    html.Div([
        html.Button("Add Row", className="my-btn"),
        html.Button("Export to Excel", className="my-btn")
    ])
])