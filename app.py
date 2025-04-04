import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    title='w3school-css',
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server  # Required for Gunicorn
  
app.layout = html.Div([
    html.P('w3school CSS'),
])

if __name__ == "__main__":
      app.run(debug=True)