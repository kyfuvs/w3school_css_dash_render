import dash_bootstrap_components as dbc
from dash import html, dcc,callback, Input, Output, State,callback_context
from pageFolder.cssFolder.css_sidebarFolder.header_css_sidebar import header_css_sidebar_layout
from pageFolder.cssFolder.css_sidebarFolder.body_css_sidebarFolder.dd_css_1_basic import dd_css_1_basic_layout
toggler_css_sidebar_layout = html.Div(
    [
        dbc.Button(
            children=html.I(className="bi bi-chevron-right text-white"),
            id="toggle-button",
            n_clicks=0,
            className='bg-transparent border-0',
        ),
        dbc.Offcanvas(
            dd_css_1_basic_layout,
            id="offcanvas",
            title=header_css_sidebar_layout,
            is_open=False,
            className='custom-offcanvas',
        ),
        html.P(id='return_is_open', children=[])
    ]
)

@callback(
    [Output("offcanvas", "is_open"),
     Output("toggle-button", "children")],
    [Input("toggle-button", "n_clicks"),
     Input("css_sidebar_is_open", "data")],
    [State("offcanvas", "is_open")]
)

# def toggle_offcanvas(n_clicks,is_open):
def toggle_offcanvas(n_clicks, sidebar_state, is_open):
    triggered_id = callback_context.triggered_id

    if triggered_id == "toggle-button":
        if n_clicks%2==1:
            return not is_open, html.I(className="bi bi-chevron-right text-white")
        elif n_clicks%2==0:
            return not is_open,html.I(className="bi bi-chevron-left text-white")
        return is_open,html.I(className="bi bi-chevron-left text-white")
    
    if triggered_id == "css_sidebar_is_open":
            if sidebar_state:
                return is_open, html.I(className="bi bi-chevron-left text-white")
            else:
                return not is_open, html.I(className="bi bi-chevron-right text-white")

    # Default case (no trigger or unknown trigger)
    return is_open, html.I(className="bi bi-chevron-right text-white")
   
