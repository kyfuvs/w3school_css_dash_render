import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    title='bs_dash_render',
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server  # Required for Gunicorn
  
app.layout = html.Div([
    html.P('Hello'),
])

if __name__ == "__main__":
      app.run_server(debug=True)