import dash
from dash import html,dcc,callback,Input,Output
import dash_bootstrap_components as dbc
from components.navbar import navbar_layout
from components.content import content_layout
from pageFolder.home import home_layout
from pageFolder.cssFolder.css import css_layout
from app_link_css import app_link_CSS
from app_link_bs import app_link_BS

app = dash.Dash(
    __name__,
    title='w3school-css',
    assets_folder='assets',
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
       return [home_layout]
    # elif pathname == '/css_basic/home':
    #     return[css_1_basic_1_home_layout]
    elif pathname.startswith('/css/'):
        return [app_link_CSS(pathname)]
    # elif pathname == '/bs_basic/home':
    #     return[bs_1_basic_1_home_layout]
    # elif pathname == '/bs_basic/get_start':
    #     return[bs_1_basic_2_get_start_layout]
    elif pathname.startswith('/bs/'):
        return [app_link_BS(pathname)]

    else:
        return [html.P('404', className='fw-bold',style={'color': '#0d6efd'})] 
if __name__ == "__main__":
      app.run(debug=True)