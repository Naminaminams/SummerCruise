import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  



packbackground = html.Div(
    [
        dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/backgrounds/bg3.png",
                    "img_style": {"height": "250px", "object-fit": "cover"}  # Set height and scale images
                }, 
            ],
            style={"max-height": "500px"}  # Limit the height of the carousel
        ),
        dbc.Card(
            [ 
                dbc.CardBody(
                    [
                        html.H2(html.B("February Packages"), className="card-title", style={'textAlign': 'center', 'fontFamily': "'Lobster'"}),
                        html.P(
                            [
                                "Book Exclusive Deals Today ", 
                            ], 
                            className="card-text",
                            style={'textAlign': 'center'}
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



package1 = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/packages/package3.jpg", 
                                    style={
                                        "width": "100%", 
                                        "height": "auto", 
                                        "position": "relative",
                                        
                                    }
                                ),
                                dbc.Button(
                                    "Book Now", 
                                    href="https://www.facebook.com/summercruiseresort",
                                    className="hover-btn",  # Add this class to the button
                                    style={
                                        "position": "absolute",
                                        "top": "80%",  # Adjust the position of the button
                                        "left": "20%",  # Center horizontally
                                        "transform": "translateX(-50%)",  # Horizontal centering
                                    },
                                    target="_blank" 
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
                            html.H4(html.B("Overnight + Freediving")),
                            html.P("📌1,999/ pax freedive lesson with shared room"),
                            html.P("📌2,200/ pax freedive lesson with private room"),
                            html.Br(),
                            html.P("INCLUSIONS"),
                            html.Ul([ 
                                html.Li("Coach Fee"),
                                html.Li("1 day Gear Rental"),
                                html.Li("Underwater Photo and Video"),
                                html.Li("2 Open Water Dives"),
                                html.Li("1 Pool Session"),
                                html.Li("Private room 2D1N"),
                            ]),  
                            html.Br(),  
                        ]
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ) 
            ],
            justify='center', 
            align='center',
            className="p-1"   
        ),
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("Sample Itinerary")),
                        html.P("""Start the day with an overview of the activities, 
                               followed by an introduction to essential techniques in a dry session.
                               Learn effective equalization techniques and master breathing exercises 
                               to optimize your underwater experience before we move to the deeper water.
                               Finally, we develop your skills in proper finning and duck diving 
                               to take those awesome shots!""", style={"textAlign": "justify"})
                    ], 
                    xs=12, sm=12, md=8, lg=3,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [
                                html.Thead(
                                    html.Tr(
                                        [
                                            html.Th("Time"),
                                            html.Th("Description"),
                                        ]
                                    )
                                ),
                                html.Tbody(
                                    [
                                        html.Tr([html.Td("9:00AM-9:30AM"), html.Td("Briefing and Dry Session")]),
                                        html.Tr([html.Td("9:30AM-10:00AM"), html.Td("Equalization and Breathing Exercises")]),
                                        html.Tr([html.Td("10:00AM-10:30AM"), html.Td("Stretching Routine")]),
                                        html.Tr([html.Td("10:30AM-12:00PM"), html.Td("First Session: Mastering Finning, Apnea, and Dynamic Techniques")]),
                                        html.Tr([html.Td("12:00PM-1:30PM"), html.Td("Lunch Break")]),
                                        html.Tr([html.Td("1:30PM-4:00PM"), html.Td("Second Session: Free Immersion, Line Training, Proper Duck Diving")]),
                                        html.Tr([html.Td("4:00PM onwards"), html.Td("Closing Highlights: Picture and video")]),
                                    ]
                                ),
                            ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=5,
                ),

            ],
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
)
 





package2 = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/packages/package1.jpg", 
                                    style={
                                        "width": "100%", 
                                        "height": "auto", 
                                        "position": "relative",
                                        
                                    }
                                ),
                                dbc.Button(
                                    "Book Now", 
                                    href="https://www.facebook.com/summercruiseresort",
                                    className="hover-btn",  # Add this class to the button
                                    style={
                                        "position": "absolute",
                                        "top": "80%",  # Adjust the position of the button
                                        "left": "20%",  # Center horizontally
                                        "transform": "translateX(-50%)",  # Horizontal centering
                                    },
                                    target="_blank" 
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
                            html.H4(html.B("Overnight + Intro to SCUBA Diving")),
                            html.P("📌 Experience SCUBA diving for only 4,990 for 2 pax"),  
                            html.Br(),
                                html.P("INCLUSIONS"),
                                    html.Ul([ 
                                        html.Li("Guide Fee"), 
                                        html.Li("Full Dive Gear Rental (mask and fins. boots. wetsuit. tank)"), 
                                        html.Li("2 Open Water Dives"), 
                                        html.Li("1 Pool Session"),  
                                    ]),  
                            html.Br(),  
                            html.P("Perfect for absolute beginners, this introductory diving course welcomes participants of all swimming abilities."), 
                            html.Br(),  
                        ]
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center', 
            align='center',
            className="p-1"   
        ),
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("Sample Itinerary")),
                        html.P(""" 
                               The course starts with an easy-to-follow video and explanation, 
                               providing you with basic knowledge about SCUBA diving. 
                               Then, we'll have a one-on-one practice in shallow water, ensuring you're comfortable with the 
                               equipment and techniques. 
                               Afterward, enjoy a guided one-on-one dive either at the beach 
                               or take a boat to our recommended locations, where you'll apply what you've learned in a safe, 
                               immersive environment.""", style={"textAlign": "justify"})
                    ], 
                    xs=12, sm=12, md=8, lg=3,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [
                                html.Thead(
                                    html.Tr(
                                        [
                                            html.Th("Time"),
                                            html.Th("Description"),
                                        ]
                                    )
                                ),
                                html.Tbody(
                                    [
                                        html.Tr([html.Td("9:30AM"), html.Td("Arrive at the Summer Cruise Beach House")]),
                                        html.Tr([html.Td("10:00AM"), html.Td("Lecture on basic diving knowledge with video")]),
                                        html.Tr([html.Td("10:30AM"), html.Td("Training in shallow water(One-on-One)")]),
                                        html.Tr([html.Td("11:00AM"), html.Td("Beach entry Fun Dive (One-on-One)")]), 
                                    ]
                                ),
                            ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=5,
                ),

            ],
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
) 






package3 = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/packages/package2.jpg", 
                                    style={
                                        "width": "100%", 
                                        "height": "auto", 
                                        "position": "relative",
                                        
                                    }
                                ),
                                dbc.Button(
                                    "Book Now", 
                                    href="https://www.facebook.com/summercruiseresort",
                                    className="hover-btn",  # Add this class to the button
                                    style={
                                        "position": "absolute",
                                        "top": "80%",  # Adjust the position of the button
                                        "left": "20%",  # Center horizontally
                                        "transform": "translateX(-50%)",  # Horizontal centering
                                    },
                                    target="_blank" 
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
                            html.H4(html.B("Overnight + Open Water SCUBA Diving")),
                            html.P("📌 Experience scuba diving for only 18,000/pax"),  
                            html.Br(),
                                html.P("INCLUSIONS"),
                                    html.Ul([ 
                                        html.Li("Instructor Fee"), 
                                        html.Li("Full Dive Gear Rental (mask and fins. boots. wetsuit. tank)"), 
                                        html.Li("PADI Manual, Dive Log & Online C-CAD Liscence"),
                                        html.Li("4 Open Water Dives"), 
                                        html.Li("2 Confined Water Dive Practice"),  
                                        html.Li("Private Accomodation 2D1N"),  
                                    ]), 
                            html.Br(),  
                        ]
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ) 
            ],
            justify='center', 
            align='center',
            className="p-1"   
        ),
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("Sample Itinerary")),
                        html.P(""" Ready to dive deeper? Take the next step and join our 
                               Open Water Scuba Diving course to fully experience the wonders beneath the surface!
                               Join us for two confined water practice dives (shallow water) and four open water lessons, 
                               where you'll be taught underwater skills in a safe, one-on-one environment.

                               Try our package today with the room included! 
                               """, style={"textAlign": "justify"})
                               
                    ], 
                    xs=12, sm=12, md=8, lg=3,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [
                                html.Thead(
                                    html.Tr(
                                        [
                                            html.Th("Time"),
                                            html.Th("Description"),
                                        ]
                                    )
                                ),
                                html.Tbody(
                                    [
                                        html.Tr([html.Td("7:00AM"), html.Td("Depart from Manila")]),
                                        html.Tr([html.Td("9:30AM"), html.Td("Arrive at the Summer Cruise Beach House")]),
                                        html.Tr([html.Td("10:00AM"), html.Td("Lecture on basic diving knowledge with video")]),
                                        html.Tr([html.Td("11:00AM"), html.Td("Confined Training in shallow water")]),
                                        html.Tr([html.Td("12:00PM"), html.Td("Lunch Break")]),
                                        html.Tr([html.Td("1:00PM"), html.Td("First Open Water Training (Beach entry)")]), 
                                        html.Tr([html.Td("2:00PM"), html.Td("Classroom and Video")]),
                                        html.Tr([html.Td("3:00PM"), html.Td("Second Open Water Training (Beach entry)")]), 
                                        html.Tr([html.Td("4:00PM"), html.Td("Classroom and Video")]),
                                        html.Tr([html.Td("5:00PM"), html.Td("Classroom for Academic Review")]),
                                        html.Tr([html.Td("6:00PM"), html.Td("Trial exam (Section1-4)")]),
                                        html.Tr([html.Td("6:30PM Onwards"), html.Td("Dinner, Free Time")]),  
                                    ]
                                ),
                            ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=5,
                ),

            ],
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
)  



layout = html.Div(
    [  
        packbackground,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        package1, 
                        package2,
                        package3
                    ],   
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)