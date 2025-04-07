import dash
from dash import html,dcc,callback,Input,Output
import dash_bootstrap_components as dbc
from components.navbar import navbar_layout
from components.content import content_layout
from pageFolder.home import home_layout
from pageFolder.cssFolder.css import css_layout
from pageFolder.cssFolder.css_1_basic.css_1_basic_1_home import css_1_basic_1_home_layout

# import pageFolder.cssFolder.css_sidebarFolder.toggler_css_sidebar
import pageFolder.cssFolder.css_sidebarFolder.toggler_css_sidebar

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
    elif pathname == '/css_basic/home':
        return[css_1_basic_1_home_layout]
    else:
        return [html.P('404', className='fw-bold',style={'color': '#0d6efd'})] 
if __name__ == "__main__":
      app.run(debug=True)