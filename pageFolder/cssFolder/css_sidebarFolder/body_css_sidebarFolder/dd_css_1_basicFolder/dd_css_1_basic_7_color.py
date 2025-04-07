import dash_bootstrap_components as dbc

dd_css_1_basic_7_color_layout = dbc.DropdownMenu(
    label="CSS Color",
    color='secondary',
    menu_variant="dark",
    children=[
        dbc.DropdownMenuItem("Colors", 
                             id="dd-css-1-basic-7-color-1-colors", 
                             n_clicks=0,
                             href='#'),
                            #  href="/css_basic/color/colors"),
        dbc.DropdownMenuItem("RGB"),
        dbc.DropdownMenuItem("HEX"),
        dbc.DropdownMenuItem("HSL"),
    ],
)