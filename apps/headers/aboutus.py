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
        html.Div(
            html.H4(html.B("Welcome to Summer Cruise Diving Resort"), 
                className="card-title", 
                style={'color':'white','textAlign': 'center', 'fontFamily': "'Lobster'", 'fontSize': '48px'}
            ),
            style={
                "position": "absolute", 
                "top": "50%", 
                "left": "50%", 
                "transform": "translate(-50%, -50%)",  # Center the text
                "color": "white", 
                "width": "100%", 
                "textAlign": "center"
            }
        ),
    ],
    style={"position": "relative", "max-height": "500px"}  # Make parent container relative
)



aboutusinfo = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.P(
                                """ 
                                🌊 Summer Cruise offers thrilling activities including Discover Scuba Diving,
                                PADI Open Water Scuba Diving Certification, Introduction to Freediving, Snorkeling, 
                                and Underwater Photography.
                                """, 
                                className="text-center", 
                                style={
                                    "font-size": "16px",  # Default size for larger screens
                                }
                            ), 
                        ],
                        className="d-flex flex-column text-center"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center text-center"
                ),
                dbc.Col(
                    html.Img(   
                        src="/assets/pictures/aboutpics/fish.jpg",  
                        style={"width": "100%", "height": "auto", "border-radius": "10px"},  
                        alt="Underwater Adventure"  # Add alt text for accessibility
                    ),
                    width={"size": 12}, 
                    xs=12, sm=12, md=4, lg=4,  # Adjust width for responsiveness
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)








missionvision = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [ 
                        html.Br(),
                        html.H2("Our Mission", className="text-center"),
                        html.P(""" 
                                In Summer Cruise we dedicate ourselves to delivering an
                                exceptional and unforgettable experience for our guests,
                                creating lasting memories by providing comfort and service.
                            """, 
                            className="text-center", 
                            style={
                                "font-size": "18px",  # Default size for larger screens
                            }
                        ),  

                        html.Br(),
                        html.Br(),
                        html.H2("Our Vision", className="text-center"),
                        html.P(""" 
                                We aim to be the leading dive vacation destination in the Philippines, 
                                offering unparalleled service and unforgettable adventures that
                                create lasting connections with our guests.
                            """, 
                            className="text-center", 
                            style={
                                "font-size": "18px",  # Default size for larger screens
                            }
                        ),   
                        html.Br(),
                    ],
                    xs=12, sm=12, md=5, lg=5,
                ),
            ],
            justify="center",
            align="center",
        ), 
    ]
)





# List of image sources (paths to your images)
image_sources = [
    "/assets/pictures/aboutpics/pic1.png", 
    "/assets/pictures/aboutpics/pic2.png", 
    "/assets/pictures/aboutpics/pic3.png", 
    "/assets/pictures/aboutpics/pic4.png", 
    "/assets/pictures/aboutpics/pic5.png", 
    "/assets/pictures/aboutpics/pic6.png", 

    "/assets/pictures/aboutpics/pic7.png", 
    "/assets/pictures/aboutpics/pic8.png", 
    "/assets/pictures/aboutpics/pic9.png", 
    "/assets/pictures/aboutpics/pic10.png", 
    "/assets/pictures/aboutpics/pic11.png", 
    "/assets/pictures/aboutpics/pic12.png", 
    ]


# Create a row of images dynamically
def create_image_row(start_index):
    images_to_show = min(6, len(image_sources) - start_index)  # Ensure we don't exceed the list
    return dbc.Row(
        [
            dbc.Col(
                html.Img(
                    src=image_sources[start_index + i],
                    className="clickable-image",
                    id=f"image{start_index + i + 1}",
                    style={"width": "100%", "cursor": "pointer", "height": "auto"},
                    alt=f"Image {start_index + i + 1}"  # Add alt text
                ),
                xs=4, sm=4, md=3, lg=2,
                className="p-2",  # Add padding to each column
            ) for i in range(images_to_show)  # Dynamically adjust based on images available
        ],
        justify="center",
        className="mb-3"  # Add vertical padding (top and bottom) to the row
    )

pictures = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [ 
                        create_image_row(0),  # First row of images  
                        create_image_row(6),  # Second row of images
                        html.Br(), 
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
                            html.Img(id="pic_modal", style={"width": "75%", "border-radius": "0px"}),
                            dbc.Button("<", id="pic_prevbtn", style={"position": "absolute", "left": "1px", "top": "50%"}, color="primary"),
                            dbc.Button(">", id="pic_nxtbtn", style={"position": "absolute", "right": "1px", "top": "50%"}, color="primary"),
                        ],
                        style={"position": "relative", "text-align": "center"},
                    ),
                    style={"background-color": "black"},  # Transparent background for the modal body
                ),
            ],
            id="pic_imagelarge",
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
        Output("pic_imagelarge", "is_open"),
        Output("pic_modal", "src"),
        Output("pic_prevbtn", "disabled"),
        Output("pic_nxtbtn", "disabled")
    ],
    [
        Input("image1", "n_clicks"), 
        Input("image2", "n_clicks"), 
        Input("image3", "n_clicks"),
        Input("image4", "n_clicks"), 
        Input("image5", "n_clicks"),
        Input("image6", "n_clicks"), 
        Input("image7", "n_clicks"), 
        Input("image8", "n_clicks"), 
        Input("image9", "n_clicks"),
        Input("image10", "n_clicks"), 
        Input("image11", "n_clicks"),
        Input("image12", "n_clicks"),
        Input("pic_prevbtn", "n_clicks"), 
        Input("pic_nxtbtn", "n_clicks")
    ],
    [
        State("pic_modal", "src"), 
        State("pic_imagelarge", "is_open")
    ],
    prevent_initial_call=True
)
def display_picimage(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, prev_click, next_click, current_src, is_open):
    ctx = dash.callback_context
    triggered = ctx.triggered[0]["prop_id"].split(".")[0]
    
    # Determine which image is currently displayed
    if current_src in image_sources:
        current_index = image_sources.index(current_src)
    else:
        current_index = 0
    
    # Handle which image to display
    if triggered in [f"image{i + 1}" for i in range(6)]:
        current_index = int(triggered.replace("image", "")) - 1
        return True, image_sources[current_index], current_index == 0, current_index == len(image_sources) - 1

    # Handle next and previous button clicks
    if is_open:
        if triggered == "pic_prevbtn" and current_index > 0:
            current_index -= 1
        elif triggered == "pic_nxtbtn" and current_index < len(image_sources) - 1:
            current_index += 1
        return True, image_sources[current_index], current_index == 0, current_index == len(image_sources) - 1

    return False, "", False, False



location = dbc.Container(
    [
        dbc.Row(
            [ 
                dbc.Col(width=1),
                dbc.Col(
                    [
                        html.H2("Directions to Summer Cruise", className="text-center"),  
                        html.Br(),
                         
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5(
                                            [
                                                html.B("Commute to"), " Binukbok Parking Area", html.B(" from Metro Manila")
                                            ]
                                        ),
                                        html.P(
                                            [
                                                "1. Make your way to", html.B(" Buendia DLTB Bus Terminal"), " (near Gil Puyat LRT Station). Take a bus with", html.B(" Lemery Tambo"), " Exit sign (DLTB Co.) Fare is at Php 175.",
                                                html.Br(),
                                                "2. Disembark at", html.B(" Xentro Mall"), " (terminal station).",
                                                html.Br(),
                                                "3. Take a tricycle to San Luis, Barangay Balite to ", html.B(" Binukbok parking or Summer Cruise Parking"), ". Travel time is 15 - 20 minutes and fare is at Php 200 but can be haggled down to Php 150.",
                                                html.Br(),
                                                "4. Once at the parking, contact Rose or Janet."
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            style={"margin": "10px", "display": "flex", "justify-content": "center"}  # Center the card
                        ),
 
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [ 
                                        html.H5(
                                            [
                                                html.B("Private Vehicle to"), " Binukbok Parking Area", html.B(" from Metro Manila")
                                            ]
                                        ),
                                        html.P(
                                            [
                                                "1. Waze", html.B(" Binukbok Parking Area"), " and make sure your route is along Star Toll and take the", html.B(" 3rd Lipa Exit (Lipa Tambo Exit)"), ".",
                                                html.Br(),
                                                "2. Drive through the national highway and ", html.B("exit at Cuenca, Alitagtag,"), " then turn left towards the McDonalds. Keep on the path, mostly straight along P.Laural Highway and turn right to", html.B(" Cuenca, Taal"), " (at the Jollibee).",
                                                html.Br(),
                                                "3. Follow the national highway road until you reach Muzon, there, turn left (when you see a small public marketplace) then corner right after a few meters. At Bauan, just follow the straight path until you turn left at the palengke.",
                                                html.Br(),
                                                "4. Drive straight to Brgy. Balite and ", html.B(" look for the signage Summer Cruise Parking"), " at the right.",
                                                html.Br(),
                                                "5. Once at the parking, contact Rose or Janet."
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            style={"margin": "10px", "display": "flex", "justify-content": "center"}  # Center the card
                        ),
                    ],
                    xs=12, sm=12, md=6, lg=6,   
                ),
                 
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src=app.get_asset_url('pictures/map_car.jpg'),
                                    top=True,
                                    style={'width': '100%', 'height': 'auto'}
                                ), 
                            ],
                            style={"margin": "10px", "display": "flex", "justify-content": "center"}  # Center the card
                        ),
                        dbc.Button(
                            "Get Started", 
                            color="light", 
                            href="https://maps.app.goo.gl/MXmixVjJ7NreyGK98",   
                            style={
                                "border": "1px solid black", 
                                "border-radius": "10px",      
                                "color": "black", 
                                "font-size": "14px",      
                                "width": "180px",
                                "margin": "10px auto",  # Center the button
                                "display": "block"
                            }
                        ),
                    ],
                    xs=12, sm=12, md=5, lg=4,
                ),
            ],
            align="center",
            className="mt-5"
        )
    ],
    fluid=True,
    className="pt-4 pb-4"
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
                        html.Br(),
                        
                        html.H4("Here's to your next underwater adventure!", className="text-center"), 
                        aboutusinfo,
                        html.Br(),
                            html.P(
                                """ 
                                ● ● ●
                                """, className="text-center"
                            ), 
                        html.Br(),
                        missionvision,
                        html.Br(),
                        html.Br(),
                        pictures,
                    ],  
                    className="px-4",  # Add horizontal padding (left and right)
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
                                html.H4("Excellent Quality", className="text-center"), 
                                html.P(
                                    """
                                    We strive to uphold quality service in 
                                    our work and how we teach, ensuring that 
                                    our guests experience the very best in comfort 
                                    and enjoyment throughout their stay.
                                    """, className="text-center"
                                ),
                                html.Br(),
                                html.H4("Hospitable Service", className="text-center"), 
                                html.P(
                                    """
                                    We believe in fostering an atmosphere where guests feel
                                    truly welcomed and cared for, creating meaningful and enjoyable experiences.
                                    """, className="text-center"
                                ),
                                html.Br(),
                                html.H4("Fun and Safety", className="text-center"), 
                                html.P(
                                    """
                                    We believe fun and safety go hand in hand,
                                    ensuring that every guest can fully 
                                    enjoy their time with us, knowing their well-being is always prioritized.
                                    """, className="text-center"
                                ),
                                html.Br(), 
                            ], 
                            xs=12, sm=12, md=6, lg=5,
                            className="px-4",  # Add horizontal padding (left and right)
                        ), 
                    ],
                    justify='center',    
                    align='center',   
                )
            ]
        ),  
        html.P(
            """ 
            ● ● ●
            """, className="text-center"
        ), 
        location,
        html.Br()

    ]
)


