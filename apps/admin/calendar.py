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



# Get the current month and year
now = datetime.now()
current_month = now.month
current_year = now.year

# Function to generate calendar layout
def generate_calendar(month, year):
    cal = calendar.monthcalendar(year, month)
    days_layout = html.Ul(
        style={'listStyleType': 'none', 'padding': '0', 'margin': '0'},
        children=[
            html.Li(
                html.Button(
                    str(day), 
                    id=f'day-{day}-{month}-{year}', 
                    n_clicks=0,
                    style={
                        'fontSize': '24px', 
                        'width': '60px', 
                        'height': '60px', 
                        'borderRadius': '5px', 
                        'margin': '5px', 
                        'backgroundColor': '#eee', 
                        'border': 'none'
                    }
                ) if day != 0 else ''
                for week in cal for day in week
            )
        ]
    )

    return html.Div(
        style={
            'padding': '70px 25px', 
            'width': '100%', 
            'backgroundColor': '#1abc9c', 
            'textAlign': 'center', 
            'display': 'inline-block'
        },
        children=[
            html.H2(
                calendar.month_name[month] + " " + str(year), 
                style={'color': 'white'}
            ),
            html.Ul(
                style={
                    'margin': '0', 
                    'padding': '10px 0', 
                    'backgroundColor': '#ddd',
                    'listStyleType': 'none'
                }, 
                children=[html.Li(
                    day, 
                    style={
                        'display': 'inline-block', 
                        'width': '13.6%', 
                        'color': '#666', 
                        'textAlign': 'center'
                    }
                ) for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
            ),
            days_layout
        ]
    )

# Define the app layout
layout = dbc.Container(
    [
        html.H1("Booking Calendar", style={'textAlign': 'center'}),
        dcc.Dropdown(
            id='month-dropdown',
            options=[{'label': calendar.month_name[i], 'value': i} for i in range(1, 13)],
            value=current_month,
            style={'width': '200px', 'margin': 'auto'}
        ),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(year), 'value': year} for year in range(current_year, current_year + 5)],
            value=current_year,
            style={'width': '200px', 'margin': 'auto'}
        ),
        html.Div(id='calendar', style={'textAlign': 'center'})
    ],
    fluid=True,
    style={'textAlign': 'center'}
)

# Callback to update the calendar based on selected month and year
@app.callback(
    Output('calendar', 'children'),
    [Input('month-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_calendar(selected_month, selected_year):
    return generate_calendar(selected_month, selected_year)