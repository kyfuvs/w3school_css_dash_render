from dash import html 
import dash_bootstrap_components as dbc
from pageFolder.bsFolder.bs_sidebar import bs_sidebar_layout

Row1=dbc.Row([
            dbc.Col([
                html.H3('Column 1'),
                html.P('col-sm-4', className="text-danger"),
                html.P('Some text...')
            ], sm=4, className='border'),

            dbc.Col([
                html.H3('Column 2'),
                html.P('col-sm-4', className="text-danger"),
                html.P('Some text...')
            ], sm=4, className='border'),

            dbc.Col([
                html.H3('Column 3'),
                html.P('col-sm-4', className="text-danger"),
                html.P('Some text...')
            ], sm=4, className='border'),
        ], className='mx-auto')

Row2=dbc.Row([
            dbc.Col([
                html.H3('Column 1'),
                html.P('col-sm-4', className="text-danger"),
                html.P('Some text...')
            ], width=4, className='border'),

            dbc.Col([
                html.H3('Column 2'),
                html.P('col-sm-4', className="text-danger"),
                html.P('Some text...')
            ], width=4, className='border'),

            dbc.Col([
                html.H3('Column 3'),
                html.P('col-sm-4', className="text-danger"),
                html.P('Some text...')
            ], width=4, className='border'),
        ], className='mx-auto')

bs_1_basic_1_home_layout=html.Div([
    bs_sidebar_layout,

    # -----container-fluid-------------
    dbc.Container(
    [
        html.H3("BS-5 Home"),
        html.P('container-fluid',className="text-warning fw-bold"),
       
    ],
    fluid=True, 
    className='bg-opacity-50 p-2 bg-secondary text-white text-center'
    ),

     # -----container-------------
    dbc.Container(
    [
        html.P('container',className="text-warning fw-bold p-1 mb-0 bg-secondary bg-opacity-70 text-center"),
        Row1,
        Row2,
   
    ],
      fluid=False, 
      className='mt-3 '
    ),

],style={'height': '100vh', 'overflowY': 'auto'})