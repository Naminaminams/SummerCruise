import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm




form = dbc.Form(
    [
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Room Name",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=4
                ),
                dbc.Col(
                    dbc.Input(type="text", id='room_name'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Room Type",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=4
                ),
                dbc.Col(
                    dbc.Select(
                        id='room_type',
                        options=[
                            {'label': 'Air conditioned', 'value': 'aircon'},
                            {'label': 'Fan room', 'value': 'fan'}
                        ]
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ), 
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Room Description", 
                    ],
                    width=4
                ),
                dbc.Col(
                   dbc.Textarea(
                        id='room_description', 
                        placeholder="Enter description"),
                   width=8,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Room Capacity",
                        html.Span("*", style={"color": "#F8B237"}) 
                    ],
                    width=4
                ),
                dbc.Col(
                    dbc.Input(type="number", id='room_capacity', placeholder="2"),
                    width=3,
                ), 
                dbc.Label("Adults", width=2),
            ],
            className="mb-2",
        ),


        dbc.Row(
            [
                dbc.Label(
                    [
                        "Weekend Price",
                        html.Span("*", style={"color": "#F8B237"}) 
                    ],
                    width=4
                ),
                dbc.Col(
                    dbc.Input(
                        type="number", 
                        id='room_price_wkend',
                        min=0,    
                    ),
                    width=3,
                ), 
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label("Weekday Discount", width=4),
                dbc.Col(
                    dbc.Input(
                        type="number", 
                        id='weekday_percentage',
                        min=0,     
                        max=100,  
                        value=80,
                        placeholder="80%",
                    ),
                    width=3,
                ), 
                dbc.Col(
                    dbc.Input(
                        type="number", 
                        id='room_price_wkday',
                        min=0, 
                        disabled=True  # Make it read-only for automation
                    ),
                    width=3,
                ), 

            ],
            className="mb-2",
        ), 
        html.Br(), 
    ],
    className="g-2",
)


 

# Callback to automate the weekday price as a percentage of the weekend price
@app.callback(
    Output('room_price_wkday', 'value'),
    [Input('room_price_wkend', 'value'),
     Input('weekday_percentage', 'value')]
)
def update_weekday_price(weekend_price, percentage):
    if weekend_price is None or percentage is None:
        return 0  # Default value
    return round(float(weekend_price) * (float(percentage) / 100), 2)






 
layout = html.Div(
    [  
        dbc.Row(
            [  
                dbc.Col(
                    html.H2(html.B("ADD NEW ROOM")),  
                    width="auto",  
                    style={"marginLeft": "15px", "marginRight": "15px"}   
                ),
            ],
            justify='center',    
            align='center',   
        ),
        html.Hr(), 
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Alert(id='recordroom_alert', is_open=False),
                        form 
                    ],
                    xs=11, sm=10, md=6, lg=6,
                    style={"marginLeft": "15px", "marginRight": "15px"}
                ),
            ],
            justify='center',
            align='center',
        ),
        html.Br(),
        dbc.Row(
            [ 
                dbc.Col(
                    dbc.Button("Save", color="primary",  id="recordroom_save_button", n_clicks=0),
                    width="auto"
                ),
                dbc.Col(
                    dbc.Button("Cancel", color="secondary", id="recordroom_cancel_button", n_clicks=0, href="/home"),  
                    width="auto"
                ),
            ],
            className="mb-2",
            justify='center',    
            align='center',  
        ), 
        html.Br(),
        html.Br(),
    ]
)








@app.callback(
    [
        Output('recordroom_alert', 'color'),
        Output('recordroom_alert', 'children'),
        Output('recordroom_alert', 'is_open'), 
    ],
    [
        Input('recordroom_save_button', 'n_clicks'),
    ], 
    [ 
        State('room_name', 'value'),
        State('room_type', 'value'),
        State('room_description', 'value'),
        State('room_capacity', 'value'),
        State('room_price_wkend', 'value'),
        State('room_price_wkday', 'value'), 
    ]
)

def save_room(submitbtn, room_name, room_type, room_description, 
              room_capacity, room_price_wkend, room_price_wkday):
 
    ctx = dash.callback_context 

    if not ctx.triggered:
        raise PreventUpdate

    eventid = ctx.triggered[0]['prop_id'].split('.')[0]
    if eventid != 'recordroom_save_button' or not submitbtn:
        raise PreventUpdate
 
    alert_open = True   
    alert_color = 'success'   
    alert_text = 'New room saved successfully!'   
 
    sql = """ 
        INSERT INTO booking.room (
            room_name, room_type, room_description, 
            room_capacity, room_price_wkend, room_price_wkday) 

        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (room_name, room_type, room_description, 
              room_capacity, room_price_wkend, room_price_wkday)
 
    try:
        db.modifydatabase(sql, values)   

    except Exception as e:
        alert_color = 'danger'
        alert_text = f'Error saving room: {e}'
        return [alert_color, alert_text, True]

    return [alert_color, alert_text, alert_open]

