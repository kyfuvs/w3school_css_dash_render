from dash import html
from pageFolder.bsFolder.bs_1_basic.bs_1_basic_1_home import bs_1_basic_1_home_layout
from pageFolder.bsFolder.bs_1_basic.bs_1_basic_2_get_start import bs_1_basic_2_get_start_layout
from pageFolder.bsFolder.bs_1_basic.bs_1_basic_3_container import bs_1_basic_3_container_layout

def app_link_BS(pathname):
    if pathname == '/bs/bs_basic/home':
        return[bs_1_basic_1_home_layout]
    elif pathname == '/bs/bs_basic/get_start':
        return[bs_1_basic_2_get_start_layout]
    elif pathname == '/bs/bs_basic/container':
        return[bs_1_basic_3_container_layout]
    else:
        return [html.P('404', className='fw-bold',style={'color': '#0d6efd'})] 

