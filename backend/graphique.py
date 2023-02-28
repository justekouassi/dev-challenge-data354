''' Ensembles de fonctions dessinant des graphiques
'''

import plotly.graph_objs as go

def generate_plot():
    ''' génère un graphique plotly
    '''
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker=dict(size=100)))
    graphJSON = fig.to_json()
    return graphJSON