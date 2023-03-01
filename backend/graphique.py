''' Module qui assure le dessin des graphiques
'''

import plotly.graph_objs as go


def generate_plot(x: list = [], y: list = [], title: str = ''):
    ''' génère un graphique plotly
    '''
    trace = go.Scatter(x=x, y=y, mode='markers', marker=dict(size=7))
    layout = go.Layout(title=title, xaxis=dict(
        title='Temps'), yaxis=dict(title='Indicateur'))
    figure = go.Figure(data=[trace], layout=layout)
    graphJSON = figure.to_json()
    return graphJSON
