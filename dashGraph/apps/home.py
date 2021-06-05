#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:31:30 2021

@author: sacia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:06:37 2020
@author: randon
"""

import plotly.express as px
import plotly.graph_objs as go
import random



import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app, server
import dash
import numpy as np
import functionLaby
#from apps import home  #, page1




# Dimensions initiales de la grille:
LARGEUR = 16
HAUTEUR = 16



layout = html.Div([
    dbc.Container([
        
        dbc.Row([
            dbc.Col(html.H1("Welcome to Labyrinth Generator", className="text-center")
                    , className="mb-4 mt-4")
        ]),
        
             
        
        dbc.Row([
            dbc.Col(html.H4(children='Labyrinth Generator'
                                     ))
            ]),
        dbc.Row([
            
           dbc.Col(html.H5(children='You can click on the button to generate a new Labyrinth :')                     
                    , className="mb-4")
            ]),
        
        
        
        dbc.Button("Click me", id="laby-click", className="mr-2"),
        
           
        html.Span(id="laby-output", style={"vertical-align": "middle"}),
       
     
        
        ])])

@app.callback(
    Output("laby-output", "children"), [Input("laby-click", "n_clicks")]
)
def on_button_click(n):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    if 'laby-click' in changed_id:
                
        labyrinthe = functionLaby.layGenerator (LARGEUR,HAUTEUR)
        fig = go.Figure(px.imshow((labyrinthe)))
        #hide axis
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        
        return html.Div(dcc.Graph(
        id='Laby', figure = fig))
    else:
        msg = 'None of the buttons have been clicked yet'
        return html.Div(msg)
        
        
   
