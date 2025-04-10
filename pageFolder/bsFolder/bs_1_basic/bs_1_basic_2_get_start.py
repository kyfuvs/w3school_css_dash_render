from dash import html 
from pageFolder.bsFolder.bs_sidebar import bs_sidebar_layout

bs_1_basic_2_get_start_layout=html.Div([
    bs_sidebar_layout,
    html.P('BSS Get Started', className='text-blue'),
])