import dash
from dash import html,dcc,callback,Input,Output
import dash_bootstrap_components as dbc
from components.navbar import navbar_layout
from components.content import content_layout

app = dash.Dash(
    __name__,
    title='w3school-css',
    # assets_folder='/assets',
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server  # Required for Gunicorn
  
app.layout = html.Div([
    dash.dcc.Location(id="url", refresh=False),
    navbar_layout,
    content_layout,
])

@app.callback(
    [Output('page-content','children')],
    [Input("url", "pathname")]
)
def toggle_pages(pathname):
    if pathname == '/':
       return [html.P('Home', className='fw-bold',style={'color': '#0d6efd'})]
    else:
        return [html.P('404', className='fw-bold',style={'color': '#0d6efd'})]
if __name__ == "__main__":
      app.run(debug=True)