#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:43:54 2021

@author: sacia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.PULSE]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Animal Research' 

server = app.server
app.config.suppress_callback_exceptions = True

