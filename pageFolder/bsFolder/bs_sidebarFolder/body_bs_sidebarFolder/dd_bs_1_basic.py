import dash_bootstrap_components as dbc

dd_bs_1_basic_layout = dbc.DropdownMenu(
    label="BS-5 Basic",
    color='secondary',
    id='dd-bs-1-basic',
    menu_variant="dark",
    children=[
        dbc.DropdownMenuItem("BS-5 HOME", 
                             id="dd-bs-1-basic-1-home", 
                             n_clicks=0,
                             href="/bs/bs_basic/home"),
        dbc.DropdownMenuItem("BS-5 Get Started", 
                             id="dd-bs-1-basic-2-get-start", 
                             n_clicks=0,
                             href="/bs/bs_basic/get_start"),
         dbc.DropdownMenuItem("BS-5 Container", 
                             id="dd-bs-1-basic-3-container", 
                             n_clicks=0,
                             href="/bs/bs_basic/container"),
    
    ],
)