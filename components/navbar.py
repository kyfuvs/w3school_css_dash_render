import dash_bootstrap_components as dbc
from dash import callback,Input, Output, State, html
from dash_bootstrap_components._components.Container import Container


W3SCHOOL_LOGO = "assets/images/w3schools-logo.png"
# W3SCHOOL_LOGO = "https://www.w3schools.com/images/w3schools_logo_436_2.png"

menu_bar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", href="/", id='nav-home', n_clicks=0, className="text-blue")),
        dbc.NavItem(dbc.NavLink("CSS HOME", id='nav-css', n_clicks=0, href="/css/css_basic/home", className="text-blue")),
        dbc.NavItem(dbc.NavLink("BS-5", id='nav-BS-5', n_clicks=0,href="/bs/bs_basic/home", className="text-blue")),
    ],
    className="mt-3 mt-md-0"
)



navbar_layout = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        # dbc.Col(html.Img(src=W3SCHOOL_LOGO, height="30px")),
                        dbc.Col(html.Img(src="/assets/images/w3schools-logo.png", height="30px")),
                        # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        # dbc.Col(html.Img(src=W3SCHOOL_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("W3Schools", className="ms-3 me-5 text-success text-opacity-55")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/",
                target="_blank",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse([
                menu_bar,
                # search_bar,
                ],
                
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid=True
    ),
    color="dark",
    dark=True,
   
)


# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [
     Input("navbar-toggler", "n_clicks"),
     Input("nav-home", "n_clicks"),
     Input("nav-css", "n_clicks"),
     Input("nav-BS-5", "n_clicks"),
    ],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n0,n1,n2,n3, is_open):
    if n0 or n1 or n2 or n3:
        return not is_open
    return is_open