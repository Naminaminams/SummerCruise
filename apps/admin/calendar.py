import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm

import calendar
from datetime import datetime, date



# Function to generate the calendar, now with support for range selection
def generate_calendar(year, month, selected_dates):
    cal = calendar.monthcalendar(year, month)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    calendar_table = []
    
    today = datetime.today().date()  # Fixed to use only the date, not datetime
    
    check_in = selected_dates['check_in']
    check_out = selected_dates['check_out']
    
    # Add header
    header = [html.Th(day) for day in days]
    calendar_table.append(html.Tr(header))
    
    for week in cal:
        week_row = []
        for day in week:
            if day == 0:
                week_row.append(html.Td(''))  # Empty cells for days outside the current month
            else:
                current_date = date(year, month, day)
                is_disabled = current_date < today
                is_check_in = (check_in and current_date == date.fromisoformat(check_in))
                is_check_out = (check_out and current_date == date.fromisoformat(check_out))
                is_in_range = (check_in and check_out and 
                               date.fromisoformat(check_in) <= current_date <= date.fromisoformat(check_out))
                
                # Define styles for different states
                button_style = {
                    'width': '40px',
                    'height': '40px',
                    'border-radius': '10%',
                    'text-align': 'center',
                    'margin': '2px',
                    'display': 'inline-block',
                    'border': 'none',  # Remove button border
                    'cursor': 'pointer'  # Change cursor to pointer
                }
                
                
                if is_disabled:
                    button_style['background-color'] = '#E0E0E0'
                    button_style['color'] = '#A0A0A0'
                elif is_check_in:
                    button_style['background-color'] = '#1E90FF'  # Highlight check-in
                    button_style['color'] = 'white'
                elif is_check_out:
                    button_style['background-color'] = '#FF4500'  # Highlight check-out
                    button_style['color'] = 'white'
                elif is_in_range:
                    button_style['background-color'] = '#87CEFA'  # Highlight range between check-in and check-out
                else:
                    button_style['background-color'] = '#FFFFFF'  # Default background color

                week_row.append(html.Td(
                    html.Button(
                        str(day),
                        id={'type': 'day-btn', 'date': current_date.isoformat()},
                        disabled=is_disabled,
                        style=button_style
                    )
                ))
        
        calendar_table.append(html.Tr(week_row))
    
    return html.Table(calendar_table, className='calendar')


def get_month_year_string(month, year):
    return f"{calendar.month_name[month]} {year}"


# Initial year and month (current date)
initial_year = datetime.today().year
initial_month = datetime.today().month

# Callback to update the calendars based on navigation and selected dates
@app.callback(
    [Output('calendar-div-1', 'children'),
     Output('calendar-div-2', 'children'),
     Output('month-year-display-1', 'children'),
     Output('month-year-display-2', 'children')],
    [Input('prev-month-btn', 'n_clicks'), 
     Input('next-month-btn', 'n_clicks'),
     Input('selected-dates', 'data')]
)
def update_calendars(prev_clicks, next_clicks, selected_dates):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    
    today = datetime.today().date()
    
    # Initialize current month and year
    current_month_1 = today.month
    current_year_1 = today.year

    # Determine if navigation buttons were clicked
    if 'prev-month-btn' in [btn['prop_id'] for btn in ctx.triggered]:
        current_month_1 -= 1
    elif 'next-month-btn' in [btn['prop_id'] for btn in ctx.triggered]:
        current_month_1 += 1
    
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
    calendar_1 = generate_calendar(current_year_1, current_month_1, selected_dates)
    calendar_2 = generate_calendar(current_year_2, current_month_2, selected_dates)

    # Create month-year strings for display
    month_year_display_1 = get_month_year_string(current_month_1, current_year_1)
    month_year_display_2 = get_month_year_string(current_month_2, current_year_2)

    return (calendar_1, calendar_2, month_year_display_1, month_year_display_2)

# Handle date selection logic
@app.callback(
    Output('selected-dates', 'data'),
    [Input({'type': 'day-btn', 'date': ALL}, 'n_clicks')],
    [State({'type': 'day-btn', 'date': ALL}, 'id'), State('selected-dates', 'data')]
)
def select_date(n_clicks_list, button_ids, selected_dates):
    if not any(n_clicks_list):  # No button clicked yet
        return selected_dates

    clicked_date = None
    for n_clicks, button_id in zip(n_clicks_list, button_ids):
        if n_clicks:
            clicked_date = button_id['date']  # This is already an ISO string
            break

    if clicked_date:
        if selected_dates['check_in'] is None:
            selected_dates['check_in'] = clicked_date  # Set check-in date
        elif selected_dates['check_out'] is None:
            selected_dates['check_out'] = clicked_date  # Set check-out date
        else:
            # Reset both dates if both are set
            selected_dates['check_in'] = clicked_date
            selected_dates['check_out'] = None

    return selected_dates

# Generate two calendars and layout
layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.H2("Booking Calendar", className="text-center"),
            width=12
        ),
        justify="center",  # Center the row
    ),
    dcc.Store(id="selected-date", data=""),  # To store the selected date
    dcc.Store(id='selected-dates', data={'check_in': None, 'check_out': None}),
            
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