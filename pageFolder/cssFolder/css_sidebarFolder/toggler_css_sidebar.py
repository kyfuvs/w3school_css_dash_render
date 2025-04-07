import dash_bootstrap_components as dbc
import dash
from dash import html, dcc,callback, Input, Output, State,callback_context
from pageFolder.cssFolder.css_sidebarFolder.header_css_sidebar import header_css_sidebar_layout
from pageFolder.cssFolder.css_sidebarFolder.body_css_sidebar import body_css_sidebar_layout
toggler_css_sidebar_layout = html.Div(
    [
        dbc.Button(
            children=html.I(className="bi bi-list text-white"),
            id="toggle-button",
            n_clicks=0,
            className='bg-transparent border-0',
        ),
        dbc.Offcanvas(
            body_css_sidebar_layout,
            id="offcanvas",
            title=header_css_sidebar_layout,
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
    Output("offcanvas", "is_open"),
    [
    #  Input("your-button-id", "n_clicks"),
    #  Input("navlink_id", "n_clicks")
     Input("toggle-button", "n_clicks"),
    #  Input("dd-css-1-basic", "n_clicks"),
     Input("dd-css-1-basic-1-home", "n_clicks"),
     Input('dd-css-1-basic-7-color-1-colors','n_clicks'),
    ],    
    [State("offcanvas", "is_open")],
)
def toggle_dd_offcanvas(n0,n1,n2, is_open):
    if n0 or n1 or n2 :
        return not is_open
    return is_open