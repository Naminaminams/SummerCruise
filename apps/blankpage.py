from dash import html
import dash_bootstrap_components as dbc

from app import app
from apps import commonmodules as cm

layout = html.Div(
    [
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H1("Page is not yet available"),
                        html.Hr(),

                        html.P("Hi! This page is currently in progress and is still up for adjustments. Thank you!"),
                        
                        
                    ],
                    width=9,
                    style={'marginLeft': '15px'}
                ),
            ]
        ),
        dbc.Row(
            [ 
            ]
        )
    ]
)


