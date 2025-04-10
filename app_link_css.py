from dash import html
from pageFolder.cssFolder.css_1_basic.css_1_basic_1_home import css_1_basic_1_home_layout

def app_link_CSS(pathname):
    if pathname == '/css/css_basic/home':
        return[css_1_basic_1_home_layout]
