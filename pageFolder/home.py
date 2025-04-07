from dash import html,callback,Input,Output

home_layout=html.Div(
    [
        html.P('Home', className='text-blue'),
        html.P(id='home_return_is_open', children=[])
    ]
)

@callback(
    # Output("offcanvas", "is_open", allow_duplicate=True),
    [Output('home_return_is_open','children')],
    Input("css_sidebar_is_open", "data"),
    # [State("offcanvas", "is_open")],
    # prevent_initial_call=True
)
def update_based_on_sidebar(is_open_True):
    if is_open_True:
        return [html.P('sidebar is_open')]
    return [html.P('sidebar NOT is_open')]