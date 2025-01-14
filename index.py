from dash import dcc, html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import webbrowser
from urllib.parse import urlparse, parse_qs

from app import app
from apps import commonmodules as cm 
from apps import home
from apps import blankpage

from apps.headers import aboutus, rooms, activities, amenities, events, packages
from apps.japanese import jhome, jaboutus, jrooms, jactivities, jpackages
from apps.admin import adminrooms, calendar


# Layout definition
CONTENT_STYLE = {
    "margin-top" : "1em",  
}

server = app.server


app.layout = html.Div(
    [
        html.Meta(
            name="theme-color",
            content='#286052'
        ),
        dcc.Location(id='url', refresh=True),
        dcc.Store(id="redirect-url", data=""),
        dcc.Store(id='sessionlogout', data=True, storage_type='local'),
        dcc.Store(id='currentuserid', data=-1, storage_type='local'),
        dcc.Store(id='currentrole', data=0, storage_type='local'),
        dcc.Store(id='page_mode', data=-1, storage_type='memory'),
        dcc.Store(id='view_id', data=-1, storage_type='memory'),
        dcc.Store(id='language_mode', data='default', storage_type='memory'),  # Track the selected language

        # Navbar container with default English navbar
        html.Div(
            id="navbar",
            style={
                'top': 0,
                'display': 'flex',
                'justify-content': 'space-between',
                'align-items': 'center',
                'width': '100%',
                'z-index': 1000,
                'background-color': 'white',
                'padding': '10px'
            },
            children=[
                cm.generate_navbar(),  # Default navbar in English
                dbc.Button(
                    "日本語", id="japanese-button", n_clicks=0, color="light",
                    style={
                        'margin-left': 'auto',  # Push to the rightmost part
                        'padding': '5px 15px',
                        'font-size': '14px',
                        "border": "1px solid black", 
                        "border-radius": "10px",      
                        "color": "black",   
                        "width": "100px", 
                    }
                ),

            ]
        ),

        html.Div(id='page-content'),
        html.Link(rel='icon', href='/assets/logo/sc_logo.jpg'),
        cm.up,

        # Footer container
        html.Div(
            id="footer",
            style={
                'display': 'flex',
                'justify-content': 'center',
                'width': '100%',
                "backgroundColor": "#212121",
                "color": "#C3C3C3",
                "fontSize": "14px"
            },
            children=cm.generate_footer()  # Default footer in English
        ), 
    ]
)

# Callback to update navbar and footer
@app.callback(
    [
        Output("navbar", "children"), 
        Output("footer", "children"),
        Output("redirect-url", "data"),
        
    ],
    [Input("japanese-button", "n_clicks")],
    prevent_initial_call=True
)
def update_layout(n_clicks):
    if n_clicks % 2 == 1:  # Switch to Japanese mode
        navbar = cm.generate_ja_navbar()
        button = dbc.Button(
            "ENGLISH", id="japanese-button",  n_clicks=n_clicks,  color="light",
            style={
                'margin-left': 'auto', 
                'padding': '5px 15px',
                'font-size': '14px',
                "border": "1px solid black", 
                "border-radius": "10px",      
                "color": "black",   
                "width": "100px", 
            }
        ) 
        navbar_with_button = html.Div(
            style={
                'display': 'flex',
                'justify-content': 'space-between',
                'align-items': 'center',
                'width': '100%', 
                'background-color': 'white'
            },
            children=[navbar, button]
        )
        
        footer = cm.generate_ja_footer()
        redirect_url = "/ja/home"
    else:  # Default mode
        navbar = cm.generate_navbar()
        button = dbc.Button(
            "日本語",  id="japanese-button", n_clicks=n_clicks, color="light",
            style={
                'margin-left': 'auto',  
                'padding': '5px 15px',
                'font-size': '14px',
                "border": "1px solid black", 
                "border-radius": "10px",      
                "color": "black",   
                "width": "100px", 
            }
        )
        navbar_with_button = html.Div(
            style={
                'display': 'flex',
                'justify-content': 'space-between',
                'align-items': 'center',
                'width': '100%', 
                'background-color': 'white'
            },
            children=[navbar, button]
        )
        footer = cm.generate_footer()
        redirect_url = "/"

    return navbar_with_button, footer, redirect_url









@app.callback(
    [
        Output('page-content', 'children'),
        Output('sessionlogout', 'data'),
    ],
    [
        Input('url', 'pathname')
    ],
    [
        State('sessionlogout', 'data'),
        State('currentuserid', 'data'),
        State('currentrole', 'data'),
        State('url', 'search')
    ]
)

def displaypage(pathname, sessionlogout, user_id, accesstype, search):
    mode = None
    parsed = urlparse(search)
    if parse_qs(parsed.query):
        mode = parse_qs(parsed.query)['mode'][0]
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        if eventid == 'url':
            if pathname == '/' or pathname == '/home' or pathname == '/logout':
                returnlayout = home.layout
            elif pathname == '/aboutus':
                returnlayout = aboutus.layout
            elif pathname == '/rooms':
                returnlayout = rooms.layout
            elif pathname == '/activities':
                returnlayout = activities.layout
            # elif pathname == '/amenities':
            #     returnlayout = blankpage.layout
            # elif pathname == '/booking':
            #     returnlayout = calendar.layout
            # elif pathname == '/events':
            #     returnlayout = blankpage.layout
            elif pathname == '/packages':
                returnlayout = packages.layout
            

            elif pathname == '/ja' or pathname == '/ja/home':
                returnlayout = jhome.layout
            # elif pathname == '/ja/aboutus':
            #     returnlayout = jaboutus.layout
            elif pathname == '/ja/rooms':
                returnlayout = jrooms.layout
            elif pathname == '/ja/activities':
                returnlayout = jactivities.layout 
            elif pathname == '/ja/packages':
                returnlayout = jpackages.layout
             
            else:
                returnlayout = blankpage.layout

    return [returnlayout, sessionlogout]
 

if __name__ == '__main__':  
    app.run_server(debug=True)


# if __name__ == '__main__':
#     webbrowser.open('http://127.0.0.1:8050/', new = 0, autoraise = True)
#     app.run_server(debug = False)