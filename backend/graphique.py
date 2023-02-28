''' Ensembles de fonctions dessinant des graphiques
'''

import plotly.graph_objs as go
import json


def generate_plot(x: list = [], y: list = []):
    ''' génère un graphique plotly
    '''
    fig = go.Figure(data=go.Scatter(
        x=x, y=y, mode='markers', marker=dict(size=10)))
    graphJSON = fig.to_json()
    return graphJSON
