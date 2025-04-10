from dash import html 
import dash_bootstrap_components as dbc
from pageFolder.bsFolder.bs_sidebar import bs_sidebar_layout

bs_1_basic_4_grid_layout=html.Div([
    bs_sidebar_layout,
    html.P('BSS Grid Basic', className='text-blue'),
    html.Div([
        dbc.Row([
            dbc.Col('.col', width=4, className='border py-3'),
            dbc.Col('.col', width=4, className='border py-3'),
            dbc.Col('.col', width=4, className='border py-3'),
        ], className='mx-2')

    ]),

    html.P('Responsive Columns', className='text-blue mt-4 mb-0'),
     dbc.Row([
            dbc.Col('.col-sm-3', sm=3, className='border py-3'),
            dbc.Col('.col-sm-3', sm=3, className='border py-3'),
            dbc.Col('.col-sm-3', sm=3, className='border py-3'),
            dbc.Col('.col-sm-3', sm=3, className='border py-3'),
        ], className='mx-2'),

    html.P('Two Unequal Responsive Columns', className='text-blue mt-4 mb-0'),
     dbc.Row([
            dbc.Col('.col-sm-4', sm=4, className='border py-3'),
            dbc.Col('.col-sm-8', sm=8, className='border py-3'),
        ], className='mx-2'),
      
],style={'height': '100vh', 'overflowY': 'auto'})