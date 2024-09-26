from dash import dcc, html
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
                                dbc.NavItem(dbc.NavLink("ABOUT US", href="/aboutus")),
                                dbc.NavItem(dbc.NavLink("ROOMS", href="/rooms")),
                                dbc.NavItem(dbc.NavLink("ACTIVITIES", href="/activities")),
                                dbc.NavItem(dbc.NavLink("EVENTS", href="/events")),
                                dbc.NavItem(dbc.NavLink("PACKAGES", href="/packages")), 
                                dbc.NavItem(dbc.NavLink("AMENITIES", href="/amenities")),
                                dbc.NavItem(dbc.NavLink("CONTACT US", href="/contactus")),
                            ],
                            className="ms-auto d-none d-lg-flex",  # Show on large screens
                            navbar=True,
                        ),
                        width="auto",
                        className="d-none d-lg-flex",  # Show on large screens
                    ),
                     
                    # Navbar Toggler for small screens
                    dbc.Col(
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        width="auto",
                        className="ms-auto d-md-flex d-lg-none ms-3",  # Show on small screens
                    ),

                    # Offcanvas for the menu
                    dbc.Offcanvas(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("HOME", href="/", style={'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("ABOUT US", href="/aboutus", style={'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("ROOMS", href="/rooms", style={'margin-right': '20px'})), 
                                dbc.NavItem(dbc.NavLink("ACTIVITIES", href="/activities", style={'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("EVENTS", href="/events", style={'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("PACKAGES", href="/packages", style={'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("AMENITIES", href="/amenities", style={'margin-right': '20px'})),
                                dbc.NavItem(dbc.NavLink("CONTACT US", href="/contactus")),
                            ],
                            vertical=True,  # Vertical layout for off-canvas
                            navbar=True,
                        ),
                        id="offcanvas",
                        is_open=False,
                        placement="start", 
                        style={"width": "250px"},  # Set the width of the off-canvas
                    ),
 
                    # Book Now Button
                    dbc.Col(
                        dbc.Button(
                            [
                                html.Img(
                                    src=app.get_asset_url('icons/calendar_icon.png'),
                                    style={'height': '1em', 'margin-right': '0.5em'}
                                ),
                                "BOOK NOW"
                            ],
                            color="primary",
                            className="d-md-flex align-items-center",
                        ),
                        width="auto",
                        className="ms-3",  
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

# Callback to toggle the offcanvas menu
@app.callback(
    Output("offcanvas", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n, is_open): 
    if n:
        return not is_open
    return is_open
 



                                
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
