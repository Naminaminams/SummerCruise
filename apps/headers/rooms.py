import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  


roombackground = html.Div(
    [
        dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/backgrounds/resortbg4.jpg",
                    "img_style": {"height": "500px", "object-fit": "cover"}  # Set height and scale images
                }, 
            ],
            style={"max-height": "500px"}  # Limit the height of the carousel
        ),
        dbc.Card(
            [ 
                dbc.CardBody(
                    [
                        html.H2(html.B("Rooms"), className="card-title", style={'textAlign': 'center', 'fontFamily': "'Lobster'"}),
                        html.P(
                            [
                                "Whether it's an overnight stay or a week long vacation, ",
                                html.Br(),  
                                "find the perfect staycation in Summer Cruise."
                            ], 
                            className="card-text",
                            style={'textAlign': 'center'}
                        ),   
                        html.Div(
                            dbc.Button("View Map", color="primary"),
                            style={'display': 'flex', 'justify-content': 'center'}  # Center the button
                        ),
                    ]
                )
            ],
            style={ 
                "position": "absolute",
                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",   
                "bottom": "40px",  
                "left": "50%",  
                "transform": "translateX(-50%)",  
                "zIndex": 1,  
                "width": "50%",   
                "opacity": 0.8,  
            },
        ),
    ],
    style={"position": "relative", "max-height": "500px"}  # Make parent container relative
)

  
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





room3_4card = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/rooms/room3.jpg", 
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
                dbc.Col(
                    html.Div(
                        [ 
                            html.H4(html.B("Seabreeze Nook")),
                            html.P("""Located on the second floor of the Left Wing, these rooms are perfect for group outings. 
                                   Relax in our nature-inspired rooms that blend bamboo 
                                   and local wood in its architecture.  
                                   """), 
                            html.P("Rooms can accommodate two adults."),
                            html.Br(),
                                html.P("FEATURES"),
                                    html.Ul([ 
                                        html.Li("With 2 single beds"),
                                        html.Li("Beach view"),
                                        html.Li("Air Conditioning"), 
                                        html.Li("Shared bathroom"),
                                    ]), 
                                html.P("INCLUSIVE OF"),
                                    html.Ul([
                                        html.Li("Wireless internet access"),
                                        html.Li("Free water and barako coffee"), 
                                    ]),  
                                html.Br(),  
                        ],
                        className="d-flex flex-column align-items-start"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),

            ],
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ]
)




room5_6card = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                             
                            html.H4(html.B("Seashell Shores")),
                            html.P("""Feel the calming rhythm of the ocean and escape to a rustic retreat 
                                   on our private veranda.                                    
                                   """), 
                            html.P("Rooms can accommodate two adults."),
                            html.Br(),
                                html.P("FEATURES"),
                                    html.Ul([ 
                                        html.Li("With 2 single beds"),
                                        html.Li("Beach view"),
                                        html.Li("Private veranda"),
                                        html.Li("Air Conditioning"),
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
                                    src="/assets/pictures/rooms/room5.jpg", 
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
 


room7_8card = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/rooms/room8.jpg", 
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
                dbc.Col(
                    html.Div(
                        [ 
                            html.H4(html.B("Coral Cove")),
                            html.P("""Coral Cove offers a unique blend of rustic and modern, 
                                   with cemented walls and double-deck beds. These rooms are situated on the first floor, 
                                   and it is the perfect stopover after a day at the sea.
                                   """), 
                            html.P("Rooms can accommodate two adults."),
                            html.Br(),
                                html.P("FEATURES"),
                                    html.Ul([ 
                                        html.Li("With 2 single beds"),
                                        html.Li("Pool view"),
                                        html.Li("Air Conditioning"),  
                                    ]), 
                                html.P("INCLUSIVE OF"),
                                    html.Ul([
                                        html.Li("Wireless internet access"),
                                        html.Li("Free water and barako coffee"), 
                                    ]),  
                                html.Br(),  
                        ],
                        className="d-flex flex-column align-items-start"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),

            ],
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ]
)
 




room9card = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                             
                            html.H4(html.B("Oasis")),
                            html.P("""Located at the leftmost side of the resort, 
                                   it's perfect location to wait for the sunrise. 
                                   Oasis offers breathtaking views of the beach 
                                   and the side mountain just on the first floor.
                                   """), 
                            html.P("Rooms can accommodate two adults."),
                            html.Br(),
                                html.P("FEATURES"),
                                    html.Ul([ 
                                        html.Li("With 2 single beds"),
                                        html.Li("Beach view"), 
                                        html.Li("Air Conditioning"), 
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
                                    src="/assets/pictures/rooms/room8.jpg", 
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
 


room10_11card = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/rooms/room10.jpg", 
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
                dbc.Col(
                    html.Div(
                        [ 
                            html.H4(html.B("Cliffside Nest")),
                            html.P("""High above the resort on the third floor, 
                                   Cliffside Nest is perfect for large groups. 
                                   The private loft and bamboo-nipa design evoke a rustic charm, ideal for a memorable stay.
                                   """), 
                            html.P("Rooms can accommodate ten adults."),
                            html.Br(),
                                html.P("FEATURES"),
                                    html.Ul([ 
                                        html.Li("With 2 single beds"), 
                                        html.Li("Loft style"),
                                        html.Li("Pool view"),
                                        html.Li("Air Conditioning"), 
                                        html.Li("Shared bathroom"), 
                                    ]), 
                                html.P("INCLUSIVE OF"),
                                    html.Ul([
                                        html.Li("Wireless internet access"),
                                        html.Li("Free water and barako coffee"), 
                                    ]),  
                                html.Br(),  
                        ],
                        className="d-flex flex-column align-items-start"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),

            ],
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ]
)

 
layout = html.Div(
    [
        roombackground,
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        room1_2card,
                        html.Br(),
                        room3_4card,
                        html.Br(),
                        room5_6card,
                        html.Br(),
                        room7_8card,
                        html.Br(), 
                        room9card,
                        html.Br(),
                        room10_11card,
                    ],  
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)