from dash import html 
from pageFolder.bsFolder.bs_sidebar import bs_sidebar_layout

bs_1_basic_3_container_layout=html.Div([
    bs_sidebar_layout,
    html.P('BSS Container', className='text-blue'),
    html.Div([
        html.P('.container-sm')
    ], className='container-sm border'),
    html.Div([
        html.P('.container-md')
    ], className='container-md border'),
    html.Div([
        html.P('.container-lg')
    ], className='container-lg border'),
    html.Div([
        html.P('.container-xl')
    ], className='container-xl border'),
    html.Div([
        html.P('.container-xxl')
    ], className='container-xxl border'),

    # <div class="container-sm border">.container-sm</div>
    # <div class="container-md border">.container-md</div>
    # <div class="container-lg border">.container-lg</div>
    # <div class="container-xl border">.container-xl</div>
    # <div class="container-xxl border">.container-xxl</div>
])