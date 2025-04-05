import dash_bootstrap_components as dbc
from dash import callback,Input, Output, State, html
from dash_bootstrap_components._components.Container import Container
from components.menuBar.home import home_layout
from components.menuBar.css import css_layout
from components.menuBar.bs import bs_layout


W3SCHOOL_LOGO = "assets/images/w3schools-logo.png"

menu_bar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", href="/", className="text-info")),
        dbc.NavItem(dbc.NavLink("CSS", href="/css", className="text-info")),
        dbc.NavItem(dbc.NavLink("BS-5", href="/bs5", className="text-info")),
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
                        dbc.Col(html.Img(src="/assets/images/w3schools-logo.png", height="30px")),
                        # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
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
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open