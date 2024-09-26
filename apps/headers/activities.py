import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  


activitiesbackground = html.Div(
    [
        dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/backgrounds/resortbgwide.jpg",
                    "img_style": {"height": "500px", "object-fit": "cover"}  
                }, 
            ],
            style={"max-height": "500px"}   
        ),
        dbc.Card(
            [ 
                dbc.CardBody(
                    [
                        html.H2(html.B("Activities"), className="card-title", style={'textAlign': 'center', 'fontFamily': "'Lobster'"}),
                        html.P(
                            [
                                """Explore the sea just in front of Summer Cruise and enjoy the beauty of the reefs. 
                                Check out what activities we have in store!""",
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

  
snorkelcard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("NO SWIMMING EXPERIENCE? NO PROBLEM")), 
                            html.P("""If you're up for just looking at the reefs or a 
                                   quick tampisaw you can opt for snorkeling. If you're not a fan of deep waters 
                                   but still want to enjoy the thriving marine life near 
                                   the shore this is for you."""), 
                            html.P(""),

                            html.Br(),
                            html.P(html.B("PRACTICE SKIN DIVING")), 
                            html.P("""Level up your skills by learning how to do quick dives and 
                                   get an up close view of the beachfront reefs."""),  
                            html.Ul([
                                html.Li("Entrance Fee Php 350"),
                                html.Li("Mask with Snorkel Php 150 (one day)"), 
                                html.Li("Full Snorkel Rental Php 350 (one day)"), 
                            ]),  
                            html.Br(),
                            dbc.Button("Book Now", href="/activities", className="hover-btn"),
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
 


freedivingcard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("INTRODUCTORY FREE DIVING")), 
                            html.P("""For the more experienced swimmers, we recommend trying out our freediving course, 
                                   complete with the necessary gears and tutorial on how to dive under deeper waters. 
                                   But not to worry if you're a non-swimmer, because we will make sure you can still get a fun experience."""), 
                             
                            html.Ul([
                                html.Li("Entrance Fee Php 350"),
                                html.Li("Introductory course Php 1,500"), 
                                html.Li("Academic and Open Water lesson (3 hrs) ✔ "),  
                                html.Li("Includes Rental gear (Fin and Mask with Snorkel) ✔ "), 
                                html.Li("Meals are not included"),
                            ]),  
                            html.Br(),
                            html.Div(
                                [
                                    dbc.Button("Book Now", href="/activities", className="hover-btn me-2"),  
                                    dbc.Button("View Promos", href="/activities", className="hover2-btn" ),
                                ],
                                className="d-flex flex-row justify-content-start align-items-center"  
                            ),
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
 


familycard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("FISHING")), 
                            html.P("""Catch a variety of saltwater fishes from Dalagang bukid 
                                   (Goldband or Yellow Tail Fusilier) to Tulingan (Skipjack Tuna), 
                                   we'll help you find the best fishing spots in the area."""), 
                            html.Ul([
                                html.Li("Entrance Fee Php 350"),
                                html.Li("Rental gear Php 2,500"), 
                                html.Li("Includes Bait ✔"),   
                                html.Li("Includes Boat ✔"),  
                            ]),  

                            html.P(html.B("ISLAND HOPPING")), 
                            html.P("""Though the beach front is the rocky type that 
                                   doesn't mean there are no sandy beaches near Summer Cruise. 
                                   For just P400 you can get a 20 min boat ride to explore the 
                                   next islands where there are underwater caves, 
                                   huge schools of fishes, and sandy beaches."""), 
                            html.Ul([
                                html.Li("Boat Fee per head Php 400"), 
                            ]), 
                            html.Br(), 
                            dbc.Button("Book Now", href="/activities", className="hover-btn me-2"),
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
 



Introdivecard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("INTRODUCTORY SCUBA DIVING")), 
                            html.P("""Explore the sea and all its creatures up front! 
                                   Learn about the proper equipment, breathing techniques 
                                   and the do's and don'ts while underwater with our trusty dive guide. 
                                   Not to worry if you're a first time swimmer, absolutely no swimming experience needed!"""), 
                             
                            html.Ul([ 
                                html.Li("Introductory course (Beach) Php 1,800"), 
                                html.Li("Introductory course (Boat) Php 3,600"),  
                                html.Li("Academic and Open Water lesson (1.5 hrs) ✔ "),  
                                html.Li("Includes Rental gear (Full set) ✔ "), 
                                html.Li("Inclusive of Entrance Fee ✔"),
                                html.Li("Meals are not included"),
                            ]),  
                            html.Br(),
                            html.Div(
                                [
                                    dbc.Button("Book Now", href="/activities", className="hover-btn me-2"),  
                                    dbc.Button("View Promos", href="/activities", className="hover2-btn" ),
                                ],
                                className="d-flex flex-row justify-content-start align-items-center"  
                            ),
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





opendivecard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("PADI OPEN WATER DIVER")), 
                            html.P("""Get your PADI Open Water License in just two days! 
                                   (5 confined water dives, and 4 open water dives.) 
                                   Dive up to a maximum depth of 18 meters with a 
                                   certified buddy and be equipped to plan and execute your own dives."""), 
                             
                            html.Ul([ 
                                html.Li("Open Water course (Beach) Php 14,800"),  
                                html.Li("5 Academic and 2 Open Water lessons ✔ "),  
                                html.Li("Includes Rental gear (Full set) ✔ "), 
                                html.Li("Includes PADI Manual, Log book, Online C-CARD ✔ "), 
                                html.Li("Inclusive of Entrance Fee ✔"),
                                html.Li("Meals and Room are not included"),
                            ]),  
                            html.Br(),
                            html.Div(
                                [
                                    dbc.Button("Book Now", href="/activities", className="hover-btn me-2"),  
                                    dbc.Button("View Promos", href="/activities", className="hover2-btn" ),
                                ],
                                className="d-flex flex-row justify-content-start align-items-center"  
                            ),
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




advanceddivecard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("PADI ADVANCED WATER DIVER")), 
                            html.P("""Level up your skills by diving up to 100 ft! 2 days training. 
                                   Includes 5 Open Water training dives (30-40 minutes per dive) 
                                   and 5 Academic lessons: 
                                   1) Peak Performance Buoyancy, 
                                   2) Underwater navigation, 
                                   3) Night diving, 
                                   4) Deep diving, 
                                   5) Drift diving or Digital under water imaging (underwater camera). 
                                   There are no exams and the course is designed to increase your knowledge and experience while having fun."""), 
                             
                            html.Ul([ 
                                html.Li("Advanced Water course (Beach) Php 14,800"),  
                                html.Li("5 Academic and 5 Open Water lessons ✔ "),  
                                html.Li("Includes Rental gear (Full set) ✔ "), 
                                html.Li("Includes PADI Manual, Log book, Online C-CARD ✔ "), 
                                html.Li("Inclusive of Entrance Fee ✔"),
                                html.Li("Meals and Room are not included"),
                            ]),  
                            html.Br(),
                            html.Div(
                                [
                                    dbc.Button("Book Now", href="/activities", className="hover-btn me-2"),  
                                    dbc.Button("View Promos", href="/activities", className="hover2-btn" ),
                                ],
                                className="d-flex flex-row justify-content-start align-items-center"  
                            ),
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



rescuedivecard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("RESCUE DIVE COURSE + EFR")), 
                            html.P("""An essential course for divers who want to dive more safely! 
                                   3 day lesson. Learn the ability to predict and solve underwater problems, 
                                   and acquire the knowledge and skills to do so. 
                                   The ability to anticipate will enable you to prepare and 
                                   respond to emergencies."""), 
                             
                            html.Ul([ 
                                html.Li("Open Water course (Beach) Php 14,800"),  
                                html.Li("5 Academic and 5 Open Water lessons ✔ "),  
                                html.Li("Includes Rental gear (Full set) ✔ "), 
                                html.Li("Includes PADI Manual, Log book, Online C-CARD ✔ "), 
                                html.Li("Inclusive of Entrance Fee ✔"),
                                html.Li("Meals and Room are not included"),
                            ]),  
                            html.Br(),
                            html.Div(
                                [
                                    dbc.Button("Book Now", href="/activities", className="hover-btn me-2"),  
                                    dbc.Button("View Promos", href="/activities", className="hover2-btn" ),
                                ],
                                className="d-flex flex-row justify-content-start align-items-center"  
                            ),
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



divemastercard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("DIVE MATER COURSE")), 
                            html.P("Requirements: 40 logs required at start, 60 logs required at application"), 
                            html.P("""You can choose from two types of programs: 
                                   short-term for a total of 7-days or an internship. 
                                   You will learn the knowledge and skills to organize a full diving experience. 
                                   This course is designed for club and team leaders and future instructors.
                                   If you would like to do an internship, please let us know the level you would like to start at 
                                   (it is possible to start from zero), **WEEKEND ONLY basis is also available."""),  
                            html.Ul([ 
                                html.Li("Php 40,000 +  PADI Membership fee $58/year"),   
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







 


picture_cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/diningarea.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/diningarea.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/diningarea.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/diningarea.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/diningarea.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/diningarea.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ), 
    ]
)

















layout = html.Div(
    [
        activitiesbackground,
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("Swimming, Snorkeling, Skin Diving"), style={'textAlign': 'center'}),
                        snorkelcard,
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("Family Bonding Activities"), style={'textAlign': 'center'}),
                        familycard,
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("Go Tankless"), style={'textAlign': 'center'}),
                        freedivingcard,
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("SCUBA Diving"), style={'textAlign': 'center'}),
                        Introdivecard, 
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("SCUBA Diving Certification"), style={'textAlign': 'center'}),
                        opendivecard, 
                        html.Br(),
                        html.Br(),
                        advanceddivecard, 
                        html.Br(),
                        html.Br(),
                        rescuedivecard, 
                        html.Br(),
                        html.Br(),
                        divemastercard, 
                        html.Br(),
                        html.Br(),
                        picture_cards,
                        html.Br(),
                        html.Br(),
 
                    ],  
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)