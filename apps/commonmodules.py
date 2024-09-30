import dash
from dash import html, dcc, callback_context
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output, State

from app import app
from apps import dbconnect as db



up = html.Div(
    [ 
        dbc.Col(
            html.A("▲ Top", href="#", style={'color': 'white', 'text-decoration': 'none'}),  
            style={
                'position': 'fixed',  # Fixed position
                'bottom': '20px',  
                'right': '20px',   
                'z-index': 1000,  # Ensure it's on top of other elements
                'padding': '10px 20px',   
                'background-color': '#007bff',  
                'border': 'none',   
                'border-radius': '5px',   
                'cursor': 'pointer', 
            },
        ), 
    ]
)





def generate_navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            dbc.Row(
                [
                    # Logo and Brand
                    dbc.Col(
                        html.A(
                            dbc.NavbarBrand(
                                html.Img(
                                    src=app.get_asset_url('logo/sc_logo.jpg'),
                                    style={'height': '3em', 'margin-right': '50px'}
                                ),
                            ),
                            href="/"
                        ),
                        width="auto",
                    ),
                    
                    # Full Navbar for larger screens
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("ABOUT US", href="/aboutus", id="about-us-link")),
                                dbc.NavItem(dbc.NavLink("ROOMS", href="/rooms", id="rooms-link")),
                                dbc.NavItem(dbc.NavLink("ACTIVITIES", href="/activities", id="activities-link")),
                                dbc.NavItem(dbc.NavLink("EVENTS", href="/events", id="events-link")),
                                dbc.NavItem(dbc.NavLink("PACKAGES", href="/packages", id="packages-link")), 
                                dbc.NavItem(dbc.NavLink("AMENITIES", href="/amenities", id="amenities-link")),
                                dbc.NavItem(dbc.NavLink("CONTACT US", href="/contactus", id="contact-us-link")),
                            ],
                            className="ms-auto d-none d-lg-flex",  
                            navbar=True,
                        ),
                        width="auto",
                        className="d-none d-lg-flex",  
                    ),

                    # Navbar Toggler for small screens
                    dbc.Col(
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        width="auto",
                        className="ms-auto d-md-flex d-lg-none ms-3",   
                    ),

                    # Book Now Button
                    dbc.Col(
                        html.A(  # Wrap the button in a link
                            dbc.Button(
                                [
                                    html.Img(
                                        src=app.get_asset_url('icons/calendar_icon.png'),
                                        style={'height': '1em', 'margin-right': '0.5em'}
                                    ),
                                    "BOOK NOW"
                                ],
                                color="primary",
                                className="d-md-flex align-items-center ms-3",
                            ),
                            href="/booking",  # Set the link to the booking page
                            style={'textDecoration': 'none'}  # Optional: Remove underline from the link
                        ),
                        width="auto",
                        className="ms-auto ms-3",  
                    ),
                     
                    # Offcanvas for the menu
                    dbc.Offcanvas(  
                        dbc.Nav(
                            [
                                dbc.NavItem(
                                    dbc.NavLink(
                                        html.Img(
                                            src=app.get_asset_url('logo/sc_logo.jpg'),
                                            style={'height': '5em'}
                                        ),
                                        href="/",
                                        style={'padding': '0'}
                                    )
                                ),
                                html.Hr(), 
                                dbc.NavItem(dbc.NavLink("ABOUT US", href="/aboutus", style={'color': 'white', 'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("ROOMS", href="/rooms", style={'color': 'white', 'margin-right': '20px'})), 
                                dbc.NavItem(dbc.NavLink("ACTIVITIES", href="/activities", style={'color': 'white', 'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("EVENTS", href="/events", style={'color': 'white', 'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("PACKAGES", href="/packages", style={'color': 'white', 'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("AMENITIES", href="/amenities", style={'color': 'white', 'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("CONTACT US", href="/contactus", style={'color': 'white'})),
                            ],
                            vertical=True,
                            navbar=True,
                        ),
                        id="offcanvas",
                        is_open=False,
                        placement="start", 
                        style={
                            "width": "250px", 
                            "backgroundColor": "#1F1F1F"
                        },  
                    ),
                ],
                align="center",
                justify="between",
                className="g-0",
            ),
            fluid=True,
        ),
        color="white",
        dark=False,
        sticky="top",
    )
    return navbar



@app.callback(
    Output("offcanvas", "is_open"),
    [Input("navbar-toggler", "n_clicks"),
     Input("about-us-link", "n_clicks"),
     Input("rooms-link", "n_clicks"),
     Input("activities-link", "n_clicks"),
     Input("events-link", "n_clicks"),
     Input("packages-link", "n_clicks"),
     Input("amenities-link", "n_clicks"),
     Input("contact-us-link", "n_clicks")],
    State("offcanvas", "is_open")  # Use State to check current state
)
def toggle_offcanvas(n_clicks, *args):
    ctx = callback_context
    if not ctx.triggered:
        return False  # Default state

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "navbar-toggler":
        return not ctx.states["offcanvas.is_open"]  # Toggle the state
    else:
        return False 

                                
def generate_footer():
    footer = dbc.Container(
        [
            dbc.Row(
                [  
                    dbc.Col(
                        [ 
                            html.Div(
                                [
                                    html.P(
                                        html.B("SPECIAL OFFERS"), 
                                        className="d-flex align-items-center text-center text-sm-left" 
                                    ),
                                    dbc.NavItem(dbc.NavLink("Events", href="/events", className="text-center text-sm-left", style={"color": "#C3C3C3"})),
                                    dbc.NavItem(dbc.NavLink("Packages", href="/packages", className="text-center text-sm-left", style={"color": "#C3C3C3"})),
                                    dbc.NavItem(dbc.NavLink("Amenities", href="/amenities", className="text-center text-sm-left", style={"color": "#C3C3C3"})),
                                ],
                                className="d-flex flex-column align-items-center align-items-sm-start"  
                            ),
                        ],
                        xs=12, sm=12, md=3, lg=3,   
                        className="d-flex justify-content-center justify-content-sm-start  mb-4" 
                    ),
                    html.Br(),
                    dbc.Col(
                        [ 
                            html.Div(
                                [
                                    html.P(
                                        html.B("REACH US AT"), 
                                        className="d-flex align-items-center text-center text-sm-left"  # Center text on small screens and align left on larger screens
                                    ),
                                    html.Br(),
                                    html.Div(
                                        [
                                            html.Img(
                                                src=app.get_asset_url('icons/location.png'),
                                                style={'height': '1em', 'margin-right': '10px'}  # Adjust size and margin as needed
                                            ),
                                            html.P("Brgy. Balite, San Luis, Batangas City", className="text-center text-sm-left"),
                                        ],
                                        className="d-flex align-items-center justify-content-center justify-content-sm-start"  # Center content on small screens
                                    ),
                                    html.Div(
                                        [
                                            html.Img(
                                                src=app.get_asset_url('icons/phone.png'),
                                                style={'height': '1em', 'margin-right': '10px'}
                                            ),
                                            html.P("+63 947 812 7671 (SMART)", className="text-center text-sm-left"),
                                        ],
                                        className="d-flex align-items-center justify-content-center justify-content-sm-start"  # Center content on small screens
                                    ),
                                    html.Div(
                                        [
                                            html.Img(
                                                src=app.get_asset_url('icons/mail.png'),
                                                style={'height': '1em', 'margin-right': '10px'}
                                            ),
                                            html.P("summercruise07@gmail.com", className="text-center text-sm-left"),
                                        ],
                                        className="d-flex align-items-center justify-content-center justify-content-sm-start"  # Center content on small screens
                                    ),
                                ],
                                className="d-flex flex-column align-items-center align-items-sm-start"  # Center items on small screens and align left on larger screens
                            ),
                        ],
                        xs=12, sm=12, md=4, lg=4,  # Responsive widths for different screen sizes
                        className="d-flex justify-content-center justify-content-sm-start"  # Center column on small screens
                    ),
                    html.Br(),

                    dbc.Col(
                        [ 
                            html.Div(
                                [
                                    dbc.Row(
                                        dbc.Col(
                                            html.P(html.B("CONNECT WITH US"), className="text-center text-sm-left")
                                        )
                                    ),
                                    dbc.Row(
                                        [ 
                                            dbc.Col(
                                                [  
                                                    html.A(
                                                        html.Img(
                                                            src=app.get_asset_url('icons/facebook_logo.png'),
                                                            style={'height': '2em', 'margin-right': '20px'}   
                                                        ),
                                                        href="https://www.facebook.com/summercruiseresort"
                                                    ),
                                                    html.A(
                                                        html.Img(
                                                            src=app.get_asset_url('icons/instagram_logo.png'),
                                                            style={'height': '2em'}
                                                        ),
                                                        href="https://www.instagram.com/summercruiseresort/"
                                                    ),
                                                ],
                                                className="d-flex justify-content-start align-items-center"  
                                            )
                                        ],
                                        className="g-2 justify-content-sm-start justify-content-lg-start"  
                                    )
                                ],
                                className="d-flex flex-column align-items-center align-items-sm-start"  # Center items on small screens and align left on larger screens
                            ),
                        ],
                        xs=12, sm=12, md=3, lg=3,  
                        className="d-flex justify-content-center justify-content-sm-start" 
                    ),
                ],
                className="mt-4 justify-content-center"
            ), 
            dbc.Row(
                dbc.Col(
                    html.P("©2024 Summer Cruise Diving Resort. All rights reserved.", className="text-center"),
                    width=12,  # Full width of the container
                    className="mt-4"
                ),
                className="justify-content-center"
            ),
            html.Br(), 
            html.Br(), 
            html.Br(), 
        ],
        fluid=True,   
        style={"max-width": "80%", "margin": "0 auto"}  # Center the container and set max-width to 80%
    )
    return footer
