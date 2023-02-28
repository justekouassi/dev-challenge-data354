import email
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .graphique import generate_plot

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    ''' représente la page principale de notre application
    qui affiche la visualisation des données prises l'un des
    capteurs en fonction d'une période donnée
    '''
    graphJSON = generate_plot()
    return render_template('index.html', title='Accueil', email=current_user.email, graphJSON=graphJSON)


@main.route('/graph')
def graph():
    graphJSON = generate_plot()
    return graphJSON


@main.route('/prediction')
def prediction() -> str:
    ''' assure la prédiction
    '''
    return render_template('prediction.html', title='Prédiction')

