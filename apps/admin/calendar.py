import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm

import calendar
from datetime import datetime 



def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    calendar_table = []
    
    # Add header with days
    header = [html.Th(day) for day in days]
    calendar_table.append(html.Tr(header))

    # Add the weeks
    for week in cal:
        week_row = []
        for day in week:
            if day == 0:
                week_row.append(html.Td(''))  # Empty cells for days outside the current month
            else:
                week_row.append(html.Td(
                    html.Button(
                        str(day),
                        id={'type': 'day-btn', 'index': day},
                        style={ 
                            'min-width': '40px',   
                            'max-width': '40px',   
                            'min-height': '40px',   
                            'max-height': '40px',   
                            'border-radius': '10%',  # Rounded corners
                            'text-align': 'center',
                            'margin': '0px',
                            'display': 'flex',  # Flexbox for button
                            'align-items': 'center',  # Center text vertically
                            'justify-content': 'center',  # Center text horizontally 
                            'min-font-size': '16px', 
                            'max-font-size': '16px',   
                        }
                    ),
                    style={'padding': '0px'}
                ))
        calendar_table.append(html.Tr(week_row))

    return html.Table(
        calendar_table, 
        className='calendar', 
        style={'width': '100%', 'border-spacing': '0px', 'border-collapse': 'collapse'}  
    )


def get_month_year_string(month, year):
    return f"{calendar.month_name[month]} {year}"


# Initial year and month (current date)
initial_year = datetime.today().year
initial_month = datetime.today().month


# Callback to update the two calendars when buttons are clicked
@app.callback(
    [Output('calendar-div-1', 'children'),
     Output('calendar-div-2', 'children'),
     Output('month-year-display-1', 'children'),
     Output('month-year-display-2', 'children')],
    [Input('prev-month-btn', 'n_clicks'), Input('next-month-btn', 'n_clicks')],
    [State('month-year-display-1', 'children'), State('month-year-display-2', 'children')]
)
def update_calendars(prev_clicks, next_clicks, current_display_1, current_display_2):
    # Extract the current month and year from the first displayed month
    if current_display_1:
        current_month_1, current_year_1 = current_display_1.split(" ")
        current_month_1 = list(calendar.month_name).index(current_month_1)  # Convert month name to index
        current_year_1 = int(current_year_1)
    else:
        current_month_1 = initial_month
        current_year_1 = initial_year
    
    # Adjust the first month based on which button is clicked
    change = next_clicks - prev_clicks
    current_month_1 += change

    # Handle year rollover for the first month
    if current_month_1 > 12:
        current_month_1 = 1
        current_year_1 += 1
    elif current_month_1 < 1:
        current_month_1 = 12
        current_year_1 -= 1

    # Set the second month (always the next consecutive month)
    current_month_2 = current_month_1 + 1
    current_year_2 = current_year_1
    if current_month_2 > 12:
        current_month_2 = 1
        current_year_2 += 1

    # Generate the updated calendars and the month-year displays
    calendar_1 = generate_calendar(current_year_1, current_month_1)
    calendar_2 = generate_calendar(current_year_2, current_month_2)

    return (calendar_1, calendar_2, 
            get_month_year_string(current_month_1, current_year_1), 
            get_month_year_string(current_month_2, current_year_2))

# Callback to handle date selection
@app.callback(
    Output('date-output', 'children'),
    [Input({'type': 'day-btn', 'index': dash.dependencies.ALL}, 'n_clicks')],
    [State('month-year-display-1', 'children'), State('month-year-display-2', 'children')]
)
def display_selected_date(n_clicks, current_display_1, current_display_2):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "No date selected"
    
    # Get the selected button
    selected_day = ctx.triggered[0]['prop_id'].split('.')[0]
    selected_day = eval(selected_day)['index']  # Extract the day number

    # Determine which calendar was clicked (first or second)
    triggered_element = ctx.triggered[0]['prop_id']
    if 'calendar-div-1' in triggered_element:
        current_month, current_year = current_display_1.split(" ")
    else:
        current_month, current_year = current_display_2.split(" ")

    current_month = list(calendar.month_name).index(current_month)
    current_year = int(current_year)

    # Return the selected date
    selected_date = f"{current_year}-{current_month:02d}-{selected_day:02d}"
    return f"Selected Date: {selected_date}"


layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.H2("Booking Calendar", className="text-center"),
            width=12
        ),
        justify="center",  # Center the row
    ),
    dcc.Store(id="selected-date", data=""),  # To store the selected date
    html.Br(),
    dbc.Row([

        # Card 1: Previous Month
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Button("<", id="prev-month-btn", n_clicks=0, className="btn btn-outline-primary"),
                                width="auto",
                                className="text-left" 
                            ),
                            dbc.Col(
                                html.Span(id="month-year-display-1", style={'fontSize': '20px', 'marginBottom': '20px', 'marginLeft': '20px'}),
                                width=8,  # Adjust width as needed to allow centering
                                className="text-center"  # Center the text
                            ),
                        ],
                        justify="start",  # Align items to the left
                        align="center"
                    ),
                    html.Div(id='calendar-div-1', style={'textAlign': 'center'})  
                ]),
            ]),
            xs=10, sm=10, md=6, lg=4
        ),
        html.Br(),
        html.Br(),

        # Card 2: Next Month
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Span(id="month-year-display-2", style={'fontSize': '20px', 'marginBottom': '20px', 'marginRight': '20px'}),
                                width=8,   
                                className="text-center"  
                            ),
                            dbc.Col(
                                html.Button(">", id="next-month-btn", n_clicks=0, className="btn btn-outline-primary"),
                                width="auto",
                                className="text-Right" 
                            ),
                            
                        ],
                        justify="end",   
                        align="center"
                    ),
                    html.Div(id='calendar-div-2', style={'textAlign': 'center'})  
                ]),
            ]),
            xs=10, sm=10, md=6, lg=4
        ),  
    ]),
    html.Hr(),
    dbc.Row(
        dbc.Col(
            html.Div(id="date-output", className="text-center"),  # Show selected date in the center
            width=12
        )
    )
])