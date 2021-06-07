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

#from apps import home  #, page1

# fonction parcours en profondeur

def dfs(s) :
    P,Q={s :None},[s]
    while Q :
        u = Q[-1]
        R=[y for y in voisinage(u) if y not in P]
       
        if R :
            v=random.choice(R)
            P[v]=u
            Q.append(v)
        else :
            Q.pop()
    return P

def voisinage(couple):
    """
    Renvoie la liste des cellules voisines
    de la cellule (ligne, colonne) = couple dans la grille.
    """
    listeVoisins = []
    
    i, j = couple[0], couple[1]
    for d in (-1, 1):
        if -1 < i+d < HAUTEUR: listeVoisins.append( (i+d, j) )
        if -1 < j+d < LARGEUR: listeVoisins.append( (i, j+d) )
        
    return listeVoisins

# Trouver un chemin dans le labyrinthe
def find_path(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path 
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                return newpath 
            

# une fonction qui permet de convertir le parcous récupéré par dfs

def convDic (d):
    dic_new = {}
    for i in d.keys():
        dic_new[i] = [d[i]]
        if d[i] in dic_new.keys():
            dic_new[d.get(i)].append(i)
    for i in d.keys():
        dic_new[i] = {node : 1 for node in dic_new[i] if node != None }
    return dic_new

# une fonction qui permet de colorier le chemin

def ColerPath (parcours, path): 
    labyrinthe = [ [0 for j in range(2*LARGEUR+1)] for i in range(2*HAUTEUR+1)] 
    
    #print(parcours)
    for i,j in parcours:
        labyrinthe[2*i+1][2*j+1] = 3
        if (i,j) !=  (0,0):
            k,l = parcours[(i,j)]
            labyrinthe[2*k+1][2*l+1] = 3
            labyrinthe[i+k+1][j+l+1] = 3
            
    for (i,j) in path:
        labyrinthe[2*i+1][2*j+1] = 5
        #if (i,j) in path: 
        if (i,j) !=  (0,0):
            k,l = parcours[(i,j)]
            labyrinthe[2*k+1][2*l+1] = 5
            labyrinthe[i+k+1][j+l+1] = 5
    labyrinthe[1][0] = 2
    labyrinthe[2*HAUTEUR-1][2*LARGEUR] = 5
    return labyrinthe

# Dimensions de la grille:
LARGEUR = 16
HAUTEUR = 16


def layGenerator(LARGEUR,HAUTEUR):
    
    dic = {(0,0) : None}
    parcours = dfs((0,0))
    dic = convDic (parcours)
    path=find_path(dic, (0, 0), (HAUTEUR-1,LARGEUR-1))
    labyrinthe = ColerPath (parcours, path)
    return labyrinthe 

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
        
        labyrinthe = layGenerator (LARGEUR,HAUTEUR)
        fig = go.Figure(px.imshow((labyrinthe)))
        #hide axis
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        
        return html.Div(dcc.Graph(
        id='Laby', figure = fig))
    else:
        msg = 'None of the buttons have been clicked yet'
        return html.Div(msg)
        
        
   
