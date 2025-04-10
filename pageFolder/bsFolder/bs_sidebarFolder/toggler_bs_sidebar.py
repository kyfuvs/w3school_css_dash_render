import dash_bootstrap_components as dbc
import dash
from dash import html, dcc,callback, Input, Output, State,callback_context
# from pageFolder.cssFolder.css_sidebarFolder.header_css_sidebar import header_css_sidebar_layout
# from pageFolder.cssFolder.css_sidebarFolder.body_css_sidebar import body_css_sidebar_layout
from pageFolder.bsFolder.bs_sidebarFolder.header_bs_sidebar import header_bs_sidebar_layout
from pageFolder.bsFolder.bs_sidebarFolder.body_bs_sidebar import body_bs_sidebar_layout
toggler_bs_sidebar_layout = html.Div(
    [
        dbc.Button(
            children=html.I(className="bi bi-list text-white"),
            id="toggle-button-bs",
            n_clicks=0,
            className='bg-transparent border-0',
        ),
        dbc.Offcanvas(
            body_bs_sidebar_layout,
            id="offcanvas-bs",
            title=header_bs_sidebar_layout,
            is_open=False,
            className='custom-offcanvas',
        ),
       
    ]
)

# @callback(
#     Output("offcanvas", "is_open"),
#     Input("toggle-button", "n_clicks"),
#     [State("offcanvas", "is_open")],
# )
# def toggle_offcanvas(n1, is_open):
#     if n1:
#         return not is_open
#     return is_open

@callback(
    Output("offcanvas-bs", "is_open"),
    [
     Input("toggle-button-bs", "n_clicks"),
     Input("dd-bs-1-basic-1-home", "n_clicks"),
     Input("dd-bs-1-basic-2-get-start", "n_clicks"),
     Input('dd-bs-1-basic-3-container','n_clicks'),
    #  Input("dd-bs-1-basic-2-get-start", "n_clicks"),
    #  Input('dd-bs-1-basic-3-container','n_clicks'),
    ],    
    [State("offcanvas-bs", "is_open")],
)
def toggle_dd_offcanvas(n0,n1,n2,n3, is_open):
    if n0 or n1 or n2 or n3:
        return not is_open
    return is_open
