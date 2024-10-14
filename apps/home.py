import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  



homepagebackground = dbc.Carousel(
    items=[
        {
            "key": "1",
            "src": "/assets/backgrounds/resortbg.jpg",
            "img_style": {"height": "500px", "object-fit": "cover"}  # Set max height and scale images
        },
        {
            "key": "2",
            "src": "/assets/backgrounds/resortbg2.jpg",
            "header": "Summer Cruise Diving Resort",
            "caption": "Your home away from home",
            "img_style": {"height": "500px", "object-fit": "cover"}  # Set max height and scale images
        },
        {
            "key": "3",
            "src": "/assets/backgrounds/resortbg3.jpg", 
            "img_style": {"height": "500px", "object-fit": "cover"}  # Set max height and scale images
        },
    ],
    style={"max-height": "500px"}  # Ensure carousel doesn't exceed the height
)



images = [
    "/assets/pictures/diningarea.jpg",
    "/assets/pictures/pool.jpg",
    "/assets/pictures/functionarea.jpg",
    "/assets/pictures/booths.jpg",
    "/assets/pictures/relax.jpg",
    "/assets/pictures/kitchen.jpg" 
]


def content(image_url, header_text, description_text):
    return dbc.Card(
        [
            dbc.CardImg(src=image_url, style={"maxHeight": "180px", "objectFit": "cover"}),
            dbc.CardHeader(
                html.H5(header_text, className="card-title fw-bold")
            ),
            dbc.CardBody(
                html.P(description_text, className="card-text")
            ),
        ],
        style={
            "maxWidth": "18rem", 
            "margin": "auto", 
            "overflow": "hidden"  # Hide overflow content
        }
    )


ammenities_cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        content(images[0], "Dining Area", "Enjoy alfresco dining with ocean views and open-air ambiance."),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[1], "Natural Salt Water Pool", "Perfect for refreshers before you hit the waves (4.5 feet max)."),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[2], "Function area", "A spacious area ideal for classes and picturesque views."),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        content(images[3], "Private Booths", "Hang out at your very own booths (inclusive of entrance fee)."),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[4], "Relaxation Areas", "Plenty of open space for the whole family to unwind."),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[5], "Kitchen", "From sashimi to inihaw, we can prepare your fresh catch."),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ), 
    ]
)








aboutus = dbc.Container(
    [
        dbc.Row(
            [ 
                dbc.Col(width=1), 
                dbc.Col(
                    [ 
                        html.Div(
                            [
                                html.H2("About Us"), 
                                html.P(
                                    """We started out as a small beach house with big dreams, 
                                    and we’ve been growing and improving ever since. 
                                    What began as a tiny kubo house with just two rooms, barely fitting five people, 
                                    has transformed into the SC we see today. 
                                    We’re proud of how far we’ve come and excited to share our journey with you.
                                    """
                                ),
                                dbc.Button("Learn More", color="light", href="/aboutus", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                            ],
                            style={   
                                "padding": "15px",  # Adds padding inside the margin for spacing 
                            }
                        ),
                    ],
                    xs=12, sm=12, md=6, lg=5
                ), 
                dbc.Col(
                    html.Img(
                        src=app.get_asset_url('pictures/grouppic.JPG'),
                        style={'width': '100%', 'height': 'auto'}
                    ), 
                    xs=12, sm=12, md=6, lg=5
                ),
                dbc.Col(width=1), 
            ],
            align="center",
            className="mt-5"
        )
    ],
    fluid=True,
    className="pt-4 pb-4"
)



location = dbc.Container(
    [
        dbc.Row(
            [ 
                dbc.Col(width=1), 
                dbc.Col(
                    html.Img(
                        src=app.get_asset_url('pictures/location.jpg'),
                        style={'width': '100%', 'height': 'auto'}
                    ), 
                    xs=12, sm=12, md=6, lg=5
                ),
                dbc.Col(
                    [ 
                        html.Div(
                            [
                                html.H2("Location"), 
                                html.P(
                                    """Located alongside the mountainous terrain of Brgy. Balite, 
                                    the beach house itself is a 10 min boat ride away from the main road 
                                    (or a 15 min walk). It is near key dive spots and marine sanctuaries 
                                    that you can easily visit via bangka.
                                    """
                                ),
                                dbc.Button("How to get there?", color="light", href="https://www.google.com/maps/dir//RWF6%2BM5F+Binukbok+Parking+Area,+Batangas/@13.824083,120.9068588,814m/data=!3m1!1e3!4m17!1m7!3m6!1s0x33bd083a59a12ae7:0x3afeb59f11b3702c!2sBinukbok+Parking+Area!8m2!3d13.8241976!4d120.9104208!16s%2Fg%2F11dxl8t656!4m8!1m0!1m5!1m1!1s0x33bd083a59a12ae7:0x3afeb59f11b3702c!2m2!1d120.9104208!2d13.8241976!3e2?entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D",   
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "180px",
                                    "margin": "20px 0"  
                                }
                            ), 
                            ],
                            style={ 
                                "padding": "15px",  # Adds padding inside the margin for spacing 
                            }
                        ),
                    ],
                    xs=12, sm=12, md=6, lg=5
                ),  
                
                dbc.Col(width=1), 
            ],
            align="center",
            className="mt-5"
        )
    ],
    fluid=True,
    className="pt-4 pb-4"
)
 




def review(image_url, header_text, description_text, small_text):
    return dbc.Card(
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.Div(
                                [
                                    dbc.CardImg(src=image_url, className="img-fluid", 
                                                style={"maxWidth": "100px", "borderRadius": "50%"}),
                                    html.Small(small_text, className="card-text text-muted text-center"),
                                ],
                                className="d-flex flex-column align-items-center"  # Center image and small text
                            ),
                            html.Br(),
                            html.H5(header_text, className="card-title text-center"),  # Center header
                            html.P(description_text, className="card-text text-center"),  # Center description
                        ]
                    ),
                    className="col-md-12",
                ),
            ],
            className="g-0 d-flex align-items-center",
        ),
        className="mb-3",
        style={"maxWidth": "540px"},
    )





review_cards = html.Div(
    [
        dbc.Row(
            [
                
                dbc.Col(
                    review(
                        "/assets/pictures/aboutus/review2.jpg", 
                        "Staff are all friendly and approachable.", 
                        """
                            First time here and we really enjoyed the activities and accommodation. Staff are all friendly and approachable.
                            We came here for the intro class, and lahat ng coaches ay mababait. They welcome questions 
                            and we learned a lot from them. Even yung coaches na hindi assigned sa inyo, mabait rin and willing to help you.
                        """, 
                        "Joshua Forcadela"
                    ),
                    xs=10, sm=10, md=3, lg=3,
                ),
                dbc.Col(
                    review(
                        "/assets/pictures/aboutus/review1.jpg", 
                        "Our experience at Summer Cruise was truly sulit and unforgettable. We almost did not want to leave! Nakakabitin!", 
                        """
                            Summer Cruise Diving Resort is one of the must-visit destinations in San Luis, Batangas. 
                            There are multiple ways to get there and for us commuters, it's via bus and tricycle. 
                            Just make sure to arrive at Summer Cruise's parking area before 4 pm to catch the boat to the resort itself...
                        """, 
                        "Nazka Leosala"
                    ),
                    xs=10, sm=10, md=3, lg=3,
                ),
                dbc.Col(
                    review(
                        "/assets/pictures/aboutus/review3.jpg", 
                        "Perfect for people on a budget", 
                        """
                            We came here on September 23-24, 2023, and it's a nice low-cost place for people who want
                            to start learning how to dive. It's perfect for people on a budget because they have 
                            packages combining accommodation and freediving intro classes. Their intro classes go as deep as 10 meters only...
                        """, 
                        "Dennise Recuerdo"
                    ),
                    xs=10, sm=10, md=3, lg=3,
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ),
    ]
)


 

 


banner = dbc.Card(
    [
        dbc.CardImg(
            src="/assets/backgrounds/resortbgwide.jpg",
            top=True,
            style={"opacity": 0.7,"height": "350px", "object-fit": "cover"},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.Div(
                        [
                            html.H4(html.B("Book today and avail our Summer Promos"), className="card-title text-center"), 

                        ],
                        className="d-flex flex-column justify-content-center align-items-center h-100",  # Center content
                        style={"height": "100%"}  # Make div take full height of card
                    ),
                ],
                className="h-100 d-flex flex-column justify-content-center align-items-center",  # Ensure card body takes full height of card and centers content
            ),
        ),
    ],
    style={ "max-height": "350px"},
)



 









reminders = html.Div(
    [
        html.H2(
            "Reminders",
            style={'textAlign': 'center', 'marginBottom': '30px'}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("We highly advise guests to come BEFORE 5pm", style={'fontWeight': 'bold'}),
                                        html.P("so you can still avail of the bangka ride going to the Resort. Otherwise, guests arriving late, regardless of number, will need to WALK to the resort, but we will have you escorted by one of our staff.")
                                    ]
                                )
                            ],
                            className="mb-3"  # Add margin bottom to card
                        ),
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("Day Trip Parking Fee - Php 50", style={'fontWeight': 'bold'}),
                                        html.P("Parking Fee is NOT included in the deposit and room rates so please prepare Php 150 (overnight)")
                                    ]
                                )
                            ],
                            className="mb-3"  # Add margin bottom to card
                        ),
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("Room Cancellation", style={'fontWeight': 'bold'}),
                                        html.P("Cancellation should be made 3 days prior check in, otherwise deposit is FORFEITED. Unless there is a weather emergency in which case the booking can be rescheduled up to the guest's needs.")
                                    ]
                                )
                            ],
                            className="mb-3"  # Add margin bottom to card
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=4,
                    className="p-1", 
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("Rocky Terrain", style={'fontWeight': 'bold'}),
                                        html.P("Although the resort is accessible by land, the path leading to the resort is rocky and might cause inconvenience to guests, especially those bringing several baggages, thus, early arrival is highly recommended.")
                                    ]
                                )
                            ],
                            className="mb-3"  # Add margin bottom to card
                        ),
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("Bangka Fee - Php 50", style={'fontWeight': 'bold'}),
                                        html.P("Bangka Fee is NOT included in the deposit and room rates so please prepare Php 50 / head (one way)")
                                    ]
                                )
                            ],
                            className="mb-3"  # Add margin bottom to card
                        ),
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("Contact Reception:", style={'fontWeight': 'bold'}),
                                        html.P("Ate Rose: 0912-366-2774"),
                                        html.P("Ate Janet: 0946-959-2298")
                                    ]
                                )
                            ],
                            className="mb-3"  # Add margin bottom to card
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=4, 
                    className="p-1", 
                ),
            ],
            className="g-0 justify-content-center"  # Center align columns within the row  # Remove gutter (spacing) between columns
        )
    ],
    style={'padding': '20px'}  # Optional: add padding around the layout
)

 
layout = html.Div(
    [
        homepagebackground, 
        html.Br(),
        html.Br(),
        html.Div(
            className="d-flex justify-content-center",  # Centers the card horizontally
            children=[
                dbc.Card(
                    dbc.Row(
                        [
                            dbc.Col(
                                [ 
                                    html.H4("Now with Starlink Wifi!", className="text-center"), 
                                ], 
                                xs=12, sm=12, md=6, lg=6,
                                className="px-4",
                            ), 
                            dbc.Col(
                                [
                                    html.Img(src="/assets/pictures/starklink.jpg", className="img-fluid rounded-start", 
                                            style={"maxWidth": "100%"}), 
                                ], 
                                xs=12, sm=12, md=6, lg=6,
                                className="px-4",
                            ), 
                        ],
                        justify='center',    
                        align='center',
                    ),
                    className="mb-3",
                    style={"maxWidth": "540px", "position": "relative", "overflow": "hidden"},  # Card styling
                )
            ]
        ),


        html.Div(
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
                                html.Br(),
                                html.P(
                                    """ 
                                    ● ● ●
                                    """, className="text-center"
                                ), 
                                html.Br(),
                                html.P(
                                    """ 
                                    For almost ten years, Summer Cruise has been serving up delicious food and comfy lodging. 
                                    With it's easy access to the sea, it's the perfect place to try your hand at water activities,
                                    be it snorkeling, free-diving, SCUBA diving, or fishing.
                                    Whether you're a couple, a family, a group of friends, traveling with your furbabies, 
                                    or a corporate team, Summer Cruise is the ideal spot for relaxation or adventure. 
                                    Escape the hustle of city life and immerse yourself in a brand new underwater world.
                                    """, className="text-center"
                                ), 
                            ], 
                            xs=12, sm=12, md=6, lg=5,
                            className="px-4",
                        ), 
                    ],
                    justify='center',    
                    align='center',   
                )
            ]
        ), 
        html.Br(),
        html.Br(),
        ammenities_cards, 
        html.Br(),  

        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("Freediving Introductory Lesson"),
                            html.P("""Let's go Tankless! Take that sisid game to the next level 
                                   by learning the basics of breath-holding techniques, 
                                   body relaxation, and how to safely dive without SCUBA gear.
                                   """),
                            dbc.Button("Learn More", color="light", href="/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "assets/pictures/home/freedivetraining.png"},
                            {"key": "2", "src": "assets/pictures/home/freedivegroup.png"},
                            {"key": "3", "src": "assets/pictures/home/freedive.png"}, 
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("Introductory SCUBA Diving"),
                            html.P("""Explore the sea and all its creatures up front! 
                                   Learn about the proper equipment, breathing techniques, and essential hand signs 
                                   while underwater with our trusty dive coaches. 
                                   Not to worry if you're a first time swimmer, 
                                   absolutely no swimming experience needed!"""),
                            dbc.Button("Learn More", color="light", href="/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0" 
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "assets/pictures/home/divetraining.png"},
                            {"key": "2", "src": "assets/pictures/home/diveguide.png"},
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("PADI Open Water SCUBA Diving"),
                            html.P("""Get your PADI Open Water License in just two days! 
                                   (5 confined water dives, and 4 open water dives.) 
                                   Dive up to a maximum depth of 18 meters with a certified buddy 
                                   and be equipped to plan and execute your own dives.."""),
                            dbc.Button("Learn More", color="light", href="/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "assets/pictures/home/turtleb.png"},
                            {"key": "2", "src": "assets/pictures/home/skindive.png"}, 
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("Advanced Water SCUBA Diving"),
                            html.P("""Build on your Open Water certification with the Advanced Water SCUBA Diving course.
                                   For just two (2) days this program introduces specialized diving techniques and advanced skills, 
                                   such as deep diving, night diving, and navigation. 
                                   Enhance your diving experience and gain confidence in more challenging underwater environments.
                                    """),
                            dbc.Button("Learn More", color="light", href="/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "assets/pictures/home/scubagroup.png"},
                            {"key": "2", "src": "assets/pictures/home/corals.png"},
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("Rescue SCUBA Diving"),
                            html.P("""An essential course for divers who want to 
                                   improve their ability to respond to emergency situations. 
                                   For a 3 day lesson learn life-saving techniques, including self-rescue, 
                                   assisting other divers, and managing underwater emergencies.  
                                   This course emphasizes safety and preparedness, 
                                   making you a more competent and confident diver."""),
                            dbc.Button("Learn More", color="light", href="/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "assets/pictures/home/turtle2.png"}, 
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("Dive Master"),
                            html.P("""The Dive Master course is a professional-level program 
                                   that prepares you for guiding and assisting other divers. 
                                   Gain extensive knowledge in dive theory, leadership skills, 
                                   and practical experience in managing dive operations. 
                                   As a Dive Master, you'll be equipped to lead dives, 
                                   conduct training sessions, and support dive instructors."""),
                            dbc.Button("Learn More", color="light", href="/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "assets/pictures/home/clownfish.png"}, 
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("Fun Dive"),
                            html.P("""Explore the local San Luis, Batangas Area: 
                                   Underwater caves, Dive sanctuaries, and noteworthy dive spots 
                                   that the locals recommend."""), 
                            dbc.Button("Learn More", color="light", href="/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "assets/pictures/home/boat.png"}, 
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(),  
        html.Div(
            [ 
                aboutus,
                location,
            ],
            style={
                "backgroundColor": "#212121",  # Black background
                "color": "white",  # White font color  
            }
        ),
        html.Br(),
        html.Br(),

        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Br(), 
                                html.H2("Guest Reviews", className="text-center"),  
                            ]
                        ),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                review_cards,  
                            ],  
                        )
                    ], className="justify-content-center align-items-center",
                ),
                dbc.Row(
                    [
                        dbc.Button("Other testimonials 🠮", color="primary", href="https://www.google.com/search?client=firefox-b-d&q=summer+cruise#lrd=0x33bd0824daf79bfb:0x308106deae431340,1,,,,", style={"width": "auto"}),
                    ], className="d-flex justify-content-center"
                )
            ]
        ),
        html.Br(),
        html.Br(),
        reminders,   
        dbc.Row(
            [
                dbc.Button("Other FAQs 🠮", color="primary", href="/", style={"width": "auto"}),
            ], className="d-flex justify-content-center"
        ),
        html.Br(),
        html.Br(),
        banner
    ]
)