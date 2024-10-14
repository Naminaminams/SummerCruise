import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import logging
 
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Set configuration
app.config.suppress_callback_exceptions = True
app.title = 'Summer Cruise Diving'

# Set up logging to suppress unnecessary server logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# If you still want to serve CSS/JS locally:
# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True

server = app.server  # Expose Flask server