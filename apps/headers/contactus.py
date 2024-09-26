import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  

 
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        
                        html.Br(),
                        html.H2("Summer Cruise Diving Resort", className="text-center"), 
                        
                        html.P(
                            """
                            ​is your perfect home away from home, nestled in the charming town of Brgy. 
                            Balite, San Luis, Batangas City. Just a two-hour drive from the metro, 
                            you'll escape the hustle and bustle and be treated to some of the best sunset views around.
                            """, className="text-center"
                        ),
                    ], 
                    xs=12, sm=12, md=6, lg=5,
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)