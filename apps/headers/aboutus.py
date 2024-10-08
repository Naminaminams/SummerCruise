import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  

 

  
room1_2card = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4(html.B("Bamboo Breeze")),
                            html.P("""Located on the second floor of the Left Wing, these rooms are situated 
                                   at the leftmost side of the resort. Feel the serenity with our bamboo and nipa rooms 
                                   as you wake up to a stunning view of the sea. 
                                   """), 
                            html.P("Rooms can accommodate two adults."),
                            html.Br(),
                                html.P("FEATURES"),
                                    html.Ul([ 
                                        html.Li("With 2 single beds"),
                                        html.Li("Beach view"),
                                        html.Li("Air Conditioning"),
                                        html.Li("Private veranda"),
                                        html.Li("Private bathroom"),
                                    ]), 
                                html.P("INCLUSIVE OF"),
                                    html.Ul([
                                        html.Li("Wireless internet access"),
                                        html.Li("Free water and barako coffee"), 
                                    ]),  
                                html.Br(),
                 
                        ],
                        className="d-flex flex-column align-items-start"  # Left-align content
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/rooms/room1.jpg", 
                                    style={
                                        "width": "100%", 
                                        "height": "auto", 
                                        "position": "relative"
                                    }
                                ),
                                dbc.Button(
                                    "Book Now", 
                                    href="/activities",
                                    className="hover-btn",  # Add this class to the button
                                    style={
                                        "position": "absolute",
                                        "top": "80%",  # Adjust the position of the button
                                        "left": "50%",  # Center horizontally
                                        "transform": "translateX(-50%)",  # Horizontal centering
                                    }
                                ),
                            ],
                            style={
                                "position": "relative",
                                "text-align": "center"
                            }
                        ),
                    ],
                    width={"size": 12, "offset": 0},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),

            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)



  
 
layout = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4(html.B("Our Mission")),
                            html.P("""In SUMMER CRUISE we dedicate ourselves to delivering an exceptional 
                                   and unforgettable experience for our guests, creating lasting memories 
                                   by providing comfort and service. 
                                   """),  
                    ],  
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)