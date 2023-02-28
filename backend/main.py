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
    # lorsque que l'utilisateur fait une recherche
    if request.method == 'POST':
        # on récupère les entrées du formulaire
        date_debut = request.form.get('date_debut')
        date_fin = request.form.get('date_fin')
        capteur = request.form.get('capteur')

        x, y = get_range_data(capteur, date_debut, date_fin)

        graphAUX1 = generate_plot(x, y['AUX1'], 'AUX1')
        graphAUX2 = generate_plot(x, y['AUX2'], 'AUX2')
        graphAUX3 = generate_plot(x, y['AUX3'], 'AUX3')
        graphCO = generate_plot(x, y['CO'], 'CO')
        graphNO2 = generate_plot(x, y['NO2'], 'NO2')
        graphO3 = generate_plot(x, y['O3'], 'O3')
        graphPM10 = generate_plot(x, y['PM10'], 'PM10')
        graphPM2_5 = generate_plot(x, y['PM2_5'], 'PM2_5')
        graphT = generate_plot(x, y['T'], 'T')
        graphRH = generate_plot(x, y['RH'], 'RH')
        graphTemp_int = generate_plot(x, y['Temp_int'], 'Temp_int')

        return render_template('index.html',
                               title='Accueil',
                               email=current_user.email,
                               graphAUX1=graphAUX1,
                               graphAUX2=graphAUX2,
                               graphAUX3=graphAUX3,
                               graphCO=graphCO,
                               graphNO2=graphNO2,
                               graphO3=graphO3,
                               graphPM10=graphPM10,
                               graphPM2_5=graphPM2_5,
                               graphT=graphT,
                               graphRH=graphRH,
                               graphTemp_int=graphTemp_int,
                               date_debut=date_debut,
                               date_fin=date_fin,
                               )

    return render_template('index.html', title='Accueil', email=current_user.email)


@main.route('/prediction')
def prediction() -> str:
    ''' affiche la page de prédiction de la qualité de l'air
    '''
    return render_template('prediction.html', title='Prédiction', email=current_user.email)
