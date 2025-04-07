import dash_bootstrap_components as dbc
from dash import callback,Input, Output, State, html
from pageFolder.cssFolder.css_sidebarFolder.toggler_css_sidebar import toggler_css_sidebar_layout

css_sidebar_layout = html.Div(
    [
        toggler_css_sidebar_layout,
    ]
)


