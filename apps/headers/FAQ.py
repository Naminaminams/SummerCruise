import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  

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
    style={'padding': '20px'}   
)



location = dbc.Container(
    [
        dbc.Row(
            [ 
                dbc.Col(width=1),
                dbc.Col(
                    [
                        html.H3("Directions to Summer Cruise", className="text-center"),  
                        html.Br(),
                         
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5(
                                            [
                                                html.B("Commute to Binukbok Parking Area from Metro Manila")
                                            ]
                                        ),
                                        html.Hr(),
                                        html.P(
                                            [
                                                "1. Make your way to", html.B(" Buendia DLTB Bus Terminal"), " (near Gil Puyat LRT Station). Take a bus with", html.B(" Lemery Tambo"), " Exit sign (DLTB Co.) Fare is at Php 175.",
                                                html.Br(),
                                                "2. Disembark at", html.B(" Xentro Mall"), " (terminal station).",
                                                html.Br(),
                                                "3. Take a tricycle to San Luis, Barangay Balite to ", html.B(" Binukbok parking or Summer Cruise Parking"), ". Travel time is 15 - 20 minutes and fare is at Php 200 but can be haggled down to Php 150.",
                                                html.Br(),
                                                "4. Once at the parking, contact Rose (0912-366-2774) or Janet (0946-959-2298)."
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
                                                html.B("Private Vehicle to Binukbok Parking Area from Metro Manila")
                                            ]
                                        ),
                                        html.Hr(),
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
                                                "5. Once at the parking, contact Rose (0912-366-2774) or Janet (0946-959-2298)."
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
    className="pt-4 pb-4", 
    id="location-section"  
)


 
questions = html.Div(
        dbc.Row( 
            dbc.Col(
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                    [
                        html.P("""
                            If you're traveling by private car, you can search for "Binukbok Parking" on Waze, 
                            Google Maps, or any other navigation app you prefer. 
                            If you're commuting, click the "More Info" button below for detailed directions. 
                            """, ),
                        html.P("""
                            Once you arrive at the parking area, contact our reception to arrange 
                            a boat transfer. If you prefer, walking to the destination is also an option.
                            """),
                        dbc.Button("More Info", id="go-to-location", href="#location-section", color="primary"),
                    ],
                    title="How do I get there?",
                    ),
                    dbc.AccordionItem(
                        [
                        html.P("""
                            We recommend taking a Bangka if you have a lot of baggage, 
                            are traveling with children or elderly companions, 
                            or are not prepared to walk through rocky terrain, 
                            as the path can be quite rough if you are not experienced.
                            """, ),
                        html.P("The Bangka is P50 per person, one way (all ages)"),
                    
                        ], title="Do I need to ride a Bangka?"
                    ),
                    dbc.AccordionItem(
                        """The parking fee is P50 for a day trip and P150 for overnight. 
                        Please note that the available parking areas are not affiliated with our resort, 
                        and payment is made directly to the local community.
                        """, title="How much is the parking fee?"
                    ),
                    dbc.AccordionItem(
                        "There is no corkage fee for food or drinks, but we do have our own restaurant if you'd like to dine with us.", 
                        title="Is there a corkage fee?"
                    ),
                    dbc.AccordionItem(
                        """A small cooking stove is available in the outdoor kitchen, 
                        but it is shared with other guests. Please also note that we do not 
                        have a spare rice cooker, and we don't allow high-voltage appliances 
                        as our solar power system cannot support them. 
                        We recommend purchasing cooked rice from our restaurant instead.""", 
                        title="Is there a kitchen available?"
                    ),
                    dbc.AccordionItem(
                        [
                            html.P("""We recommend placing your order with the restaurant in advance or as soon as you arrive 
                                (e.g. 9–10 AM or 4–5 PM) to avoid delays, as our meals are made upon order and orders 
                                can pile up once it is rush hour.
                            """),
                            html.P("We also have BBQ available: (ordered through booking)"),
                            html.Ul([
                                html.Li("BBQ Meat Set (Pork, Chicken, Vegetables, Rice) P600/ head"),
                                html.Li("BBQ Seafood Set (Fish, Mussels, Shrimp, Rice) P800/ head"),  
                            ]),  
                        ],
                        title="What time should we order food from the restaurant?"
                    ),
                    dbc.AccordionItem(
                        """Yes, but only small to medium size dogs are allowed. Please also not that we do have our own guard dog "Summer" there.
                        """, title="Are you pet friendly?"
                    ),
                    dbc.AccordionItem(
                        """Sadly, we are not accessible to persons with mobility needs.
                        The way to the resort is via bangka and there are no ramps to aid in getting off the boat.
                        """, 
                        title="Are you accessible to Persons with Disability (PWDs)?"
                    ),
                    dbc.AccordionItem(
                        "We offer a variety of Filipino and Japanese dishes, including meat, noodle, and rice meals. ", 
                        title="What food are available?"
                    ),
                ],
                flush=True
            ),
            xs=12, sm=12, md=8, lg=8
        ),
        justify="center"
    )
)


layout = html.Div(
    [
        html.Br(),
        questions,
        html.Br(),
        reminders,
        html.Br(),
        location

    ]
)