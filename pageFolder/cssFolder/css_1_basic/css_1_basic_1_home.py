from dash import html 
from pageFolder.cssFolder.css_sidebar import css_sidebar_layout

css_1_basic_1_home_layout=html.Div([
    css_sidebar_layout,
    html.P('CSS HOME',className='text-blue')
])