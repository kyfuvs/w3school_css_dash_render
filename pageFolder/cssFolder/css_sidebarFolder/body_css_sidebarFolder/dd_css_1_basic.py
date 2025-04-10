import dash_bootstrap_components as dbc
from pageFolder.cssFolder.css_sidebarFolder.body_css_sidebarFolder.dd_css_1_basicFolder.dd_css_1_basic_7_color import dd_css_1_basic_7_color_layout

dd_css_1_basic_layout = dbc.DropdownMenu(
    label="CSS Basic",
    color='secondary',
    id='dd-css-1-basic',
    menu_variant="dark",
    children=[
        dbc.DropdownMenuItem("CSS HOME", 
                             id="dd-css-1-basic-1-home", 
                             n_clicks=0,
                             href="/css/css_basic/home"),
        dbc.DropdownMenuItem("Item 2"),
        dbc.DropdownMenuItem("Item 3"),
        dd_css_1_basic_7_color_layout,
    ],
)