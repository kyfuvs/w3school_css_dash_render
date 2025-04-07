from dash import html 
import dash_bootstrap_components as dbc

header_css_sidebar_layout =dbc.Nav(
    [
      dbc.NavItem(dbc.NavLink("CSS Tutorial", 
                              href="https://www.w3schools.com/css/default.asp", 
                              target='_blank',
                              className="text-blue fs-6")),
    ],
    
)