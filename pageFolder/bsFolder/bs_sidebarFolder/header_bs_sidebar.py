from dash import html 
import dash_bootstrap_components as dbc

header_bs_sidebar_layout =dbc.Nav(
    [
      dbc.NavItem(dbc.NavLink("BS-5 Tutorial", 
                              href="https://www.w3schools.com/bootstrap5/index.php", 
                              target='_blank',
                              className="text-blue fs-6")),
    ],
    
)