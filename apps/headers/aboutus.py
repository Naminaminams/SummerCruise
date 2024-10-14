import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  

 

aboutusbackground = html.Div(
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
                        html.H2(html.B("Welcome to Summer Cruise Diving Resort"), 
                            className="card-title", 
                            style={'fontColor':'white','textAlign': 'center', 'fontFamily': "'Lobster'"}),
                         
                    ]
                )
            ],
            style={ 
                "position": "absolute", 
                "top": "100px",  
                "left": "50%",  
                "transform": "translateX(-50%)",    
            },
        ),
    ],
    style={"position": "relative", "max-height": "500px"}  # Make parent container relative
)



# List of image sources (paths to your images)
image_sources = [
    "/assets/pictures/grouppic.jpg", 
    "/assets/pictures/grouppic.jpg", 
    "/assets/pictures/grouppic.jpg",
    "/assets/pictures/grouppic.jpg", 
    "/assets/pictures/grouppic.jpg", 
    "/assets/pictures/grouppic.jpg",
    ]

mission = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H4("Our Mission", className="text-center"),
                        html.P("In SUMMER CRUISE we dedicate ourselves to delivering an", className="text-center"),
                        html.P(
                            """
                            In SUMMER CRUISE we dedicate ourselves to delivering an  
                            """,
                            className="text-center",
                        ),
                        html.Br(),
                        # Row for pictures
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[0],  # Path to image 1
                                        className="clickable-image",
                                        id="image1",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[1],  # Path to image 2
                                        className="clickable-image",
                                        id="image2",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[2],  # Path to image 3
                                        className="clickable-image",
                                        id="image3",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                            ],
                            justify="center",
                        ),
                    ],
                    xs=12, sm=12, md=9, lg=9,
                ),
            ],
            justify="center",
            align="center",
        ),
        # Modal for enlarged image with dark background
        dbc.Modal(
            [
                dbc.ModalBody(
                    html.Div(
                        [
                            html.Img(id="mission_modal", style={"width": "75%", "border-radius": "0px"}),
                            dbc.Button("<", id="mission_prevbtn", style={"position": "absolute", "left": "1px", "top": "50%"}, color="primary"),
                            dbc.Button(">", id="mission_nxtbtn", style={"position": "absolute", "right": "1px", "top": "50%"}, color="primary"),
                        ],
                        style={"position": "relative", "text-align": "center"},
                    ),
                    style={"background-color": "black"},  # Transparent background for the modal body
                ),
            ],
            id="mission_imagelarge",
            size="xl",  # Larger modal for a bigger image
            centered=True,
            backdrop=True,  # Darken background
            style={"background-color": "rgba(0, 0, 0, 0.5)"},  # Transparent modal background
        ),
    ]
)


# Callback to open the modal and display the clicked image
@app.callback(
    [
        Output("mission_imagelarge", "is_open"),
        Output("mission_modal", "src"),
        Output("mission_prevbtn", "disabled"),
        Output("mission_nxtbtn", "disabled")
    ],
    [
        Input("image1", "n_clicks"), 
        Input("image2", "n_clicks"), 
        Input("image3", "n_clicks"),  
        Input("mission_prevbtn", "n_clicks"), 
        Input("mission_nxtbtn", "n_clicks")
    ],
    [
        State("mission_modal", "src"), 
        State("mission_imagelarge", "is_open")
    ],
    prevent_initial_call=True
)
def display_missionimage(n1, n2, n3, prev_click, next_click, current_src, is_open):
    ctx = dash.callback_context
    triggered = ctx.triggered[0]["prop_id"].split(".")[0]
    
    # Determine which image is currently displayed
    if current_src:
        current_index = image_sources.index(current_src)
    else:
        current_index = 0
    
    # Handle which image to display
    if triggered in ["image1", "image2", "image3"]:
        if triggered == "image1" and n1:
            current_index = 0
        elif triggered == "image2" and n2:
            current_index = 1
        elif triggered == "image3" and n3:
            current_index = 2
        return True, image_sources[current_index], current_index == 0, current_index == len(image_sources) - 1

    # Handle next and previous button clicks
    if is_open:
        if triggered == "mission_prevbtn" and current_index > 0:
            current_index -= 1
        elif triggered == "mission_nxtbtn" and current_index < len(image_sources) - 1:
            current_index += 1
        return True, image_sources[current_index], current_index == 0, current_index == len(image_sources) - 1

    return False, "", False, False





vision = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H4("Our Vision", className="text-center"),
                        html.P(
                            """
                            We aim to be the leading dive vacation destination in the Philippines, 
                            offering unparalleled service and unforgettable adventures that 
                            create lasting connections with our guests.
                            """,
                            className="text-center",
                        ),
                        html.P(
                            """
                            We aim to be the leading dive vacation destination in the Philippines, 
                            offering unparalleled service and unforgettable adventures that 
                            create lasting connections with our guests.
                            """,
                            className="text-center",
                        ),
                        html.Br(),
                        # Row for pictures
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[0],  # Path to image 1
                                        className="clickable-image",
                                        id="image1",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[1],  # Path to image 2
                                        className="clickable-image",
                                        id="image2",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[2],  # Path to image 3
                                        className="clickable-image",
                                        id="image3",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                            ],
                            justify="center",
                        ),
                    ],
                    xs=12, sm=12, md=9, lg=9,
                ),
            ],
            justify="center",
            align="center",
        ),
        # Modal for enlarged image with dark background
        dbc.Modal(
            [
                dbc.ModalBody(
                    html.Div(
                        [
                            html.Img(id="mission_modal", style={"width": "75%", "border-radius": "0px"}),
                            dbc.Button("<", id="mission_prevbtn", style={"position": "absolute", "left": "1px", "top": "50%"}, color="primary"),
                            dbc.Button(">", id="mission_nxtbtn", style={"position": "absolute", "right": "1px", "top": "50%"}, color="primary"),
                        ],
                        style={"position": "relative", "text-align": "center"},
                    ),
                    style={"background-color": "black"},  # Transparent background for the modal body
                ),
            ],
            id="mission_imagelarge",
            size="xl",  # Larger modal for a bigger image
            centered=True,
            backdrop=True,  # Darken background
            style={"background-color": "rgba(0, 0, 0, 0.5)"},  # Transparent modal background
        ),
    ]
)

vision = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H4("Our Vision", className="text-center"),
                        html.P(
                            """
                            We aim to be the leading dive vacation destination in the Philippines, 
                            offering unparalleled service and unforgettable adventures that 
                            create lasting connections with our guests.
                            """,
                            className="text-center",
                        ),
                        html.Br(),
                        # Row for pictures
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[3],  # Path to image 1
                                        className="clickable-image",
                                        id="image4",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[4],  # Path to image 2
                                        className="clickable-image",
                                        id="image5",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                                dbc.Col(
                                    html.Img(
                                        src=image_sources[5],  # Path to image 3
                                        className="clickable-image",
                                        id="image6",
                                        style={"width": "100%", "cursor": "pointer"},
                                    ),
                                    xs=4, sm=4, md=3, lg=3,
                                ),
                            ],
                            justify="center",
                        ),
                    ],
                    xs=12, sm=12, md=9, lg=9,
                ),
            ],
            justify="center",
            align="center",
        ),
        # Modal for enlarged image with dark background
        dbc.Modal(
            [
                dbc.ModalBody(
                    html.Div(
                        [
                            html.Img(id="modal-image", style={"width": "75%", "border-radius": "0px"}),
                            dbc.Button("<", id="prev-btn", style={"position": "absolute", "left": "1px", "top": "50%"}, color="primary"),
                            dbc.Button(">", id="next-btn", style={"position": "absolute", "right": "1px", "top": "50%"}, color="primary"),
                        ],
                        style={"position": "relative", "text-align": "center"},
                    ),
                    style={"background-color": "black"},  # Transparent background for the modal body
                ),
            ],
            id="image-modal",
            size="xl",  # Larger modal for a bigger image
            centered=True,
            backdrop=True,  # Darken background
            style={"background-color": "rgba(0, 0, 0, 0.5)"},  # Transparent modal background
        ),
    ]
)







layout = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    [ 
                        aboutusbackground,  
                        html.Br(),
                        html.Br(),
                        mission,
                        html.Br(),
                        html.Br(),
                        vision,
                    ],  
                ), 
            ],
            justify='center',    
            align='center',   
        ), 
          
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                
                                html.Br(),
                                html.H4("SUMMER CRUISE commits itself to these Core Values:", className="text-center"), 
                                    html.H6("Excellent Quality", className="text-center"),
                                    html.Br(),
                                    html.P(
                                        """
                                        We strive to uphold quality service in 
                                        our work and how we teach, ensuring that 
                                        our guests experience the very best in comfort 
                                        and enjoyment throughout their stay.

                                        """, className="text-center"
                                    ),
                                html.Br(),
                                    html.H6("Hospitable Service", className="text-center"),
                                    html.Br(),
                                    html.P(
                                        """
                                        We believe in fostering an atmosphere where guests feel
                                        truly welcomed and cared for, creating meaningful and enjoyable experiences.
                                        """, className="text-center"
                                    ),
                                html.Br(),
                                    html.H6("Fun and Safety ", className="text-center"),
                                    html.Br(),
                                    html.P(
                                        """
                                        We believe fun and safety go hand in hand,
                                        ensuring that every guest can fully 
                                        enjoy their time with us, knowing their well-being is always prioritized.


                                        """, className="text-center"
                                    ),
                                html.Br(),
                                html.P(
                                    """ 
                                    ● ● ●
                                    """, className="text-center"
                                ), 
                                html.Br(), 
                            ], 
                            xs=12, sm=12, md=6, lg=5,
                        ), 
                    ],
                    justify='center',    
                    align='center',   
                )
            ]
        ), 
    ]
)


