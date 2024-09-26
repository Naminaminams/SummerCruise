import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import logging

app = dash.Dash(__name__, external_stylesheets=["assets/bootstrap.css"])

app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.title = 'Summer Cruise Diving'

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)