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

from apps.headers import aboutus, rooms, activities, amenities, booking, contactus, events, packages
from apps.admin import adminrooms, calendar


# Layout definition
CONTENT_STYLE = {
    "margin-top" : "1em",  
}

server = app.server

app.layout = html.Div(
    [
        html.Meta(
            name = "theme-color",
            content = '#286052'
        ),
        dcc.Location(id = 'url', refresh = True), 
        dcc.Store(id='sessionlogout', data = True, storage_type='local'),
        
        dcc.Store(id='currentuserid', data = -1, storage_type='local'),
        dcc.Store(id='currentrole', data = 0, storage_type='local'),
 
        dcc.Store(id = 'page_mode', data = -1, storage_type = 'memory'),
        dcc.Store(id = 'view_id', data = -1, storage_type = 'memory'), 
        
        html.Div(
            cm.generate_navbar(),
            style={ 
                'top': 0,  # Position it at the top of the viewport
                'display': 'flex',
                'justify-content': 'center',  # Center the navbar horizontally
                'width': '100%',  # Ensure it spans the full width
                'z-index': 1000,  # Ensure it stays on top of other elements
                'background-color': 'white',    
            }
        ),
        html.Div(id = 'page-content', style = CONTENT_STYLE),
        html.Link(rel='icon', href='/assets/logo/sc_logo.jpg'),
        cm.up,
        html.Div(
            cm.generate_footer(),
            style={
                'display': 'flex',
                'justify-content': 'center',  
                'width': '100%',   
                "backgroundColor": "#212121",   
                "color": "#C3C3C3", 
                "fontSize": "14px"
            }
        ), 
    ]
)

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
            elif pathname == '/amenities':
                returnlayout = adminrooms.layout
            elif pathname == '/booking':
                returnlayout = calendar.layout
            elif pathname == '/contactus':
                returnlayout = contactus.layout
            elif pathname == '/events':
                returnlayout = events.layout
            elif pathname == '/packages':
                returnlayout = packages.layout
            
             
            else:
                returnlayout = blankpage.layout

    return [returnlayout, sessionlogout]
 

#if __name__ == '__main__':
    #app.run_server(debug=True)


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new = 0, autoraise = True)
    app.run_server(debug = False)