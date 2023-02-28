''' Module de visualisation
'''

from flask import Blueprint, request, render_template, flash
from flask_login import login_required, current_user
from .api import get_range_data
from .graphique import generate_plot

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    ''' représente la page principale de notre application
    qui affiche la visualisation des données prises par l'un des
    capteurs en fonction d'une période donnée
    '''
    # générons un graphe vide par défaut
    graphJSON = generate_plot()
    # lorsque que l'utilisateur fais une recherche
    if request.method == 'POST':
        # on récupère les entrées du formulaire
        date_debut = request.form.get('date_debut')
        date_fin = request.form.get('date_fin')
        capteur = request.form.get('capteur')
        
        (x, y) = get_range_data(capteur, date_debut, date_fin)
        graphJSON = generate_plot(x, y)

    return render_template('index.html', title='Accueil', email=current_user.email, graphJSON=graphJSON)


@main.route('/graph')
def graph():
    graphJSON = generate_plot()
    return graphJSON


@main.route('/prediction')
def prediction() -> str:
    ''' affiche la page de prédiction de la qualité de l'air
    '''
    return render_template('prediction.html', title='Prédiction', email=current_user.email)
