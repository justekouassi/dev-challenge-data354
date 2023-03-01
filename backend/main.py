''' Module de visualisation 
'''

from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from .api import get_current_values_co2, get_range_data, get_single_day
from .graphique import generate_plot

# sous-application gérant la visualisation
main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    ''' route principale de notre application qui permet la visualisation 
    des valeurs des indicateurs prises par l'un des capteurs 
    en fonction d'une période donnée
    '''
    # lorsque que l'utilisateur fait une recherche
    if request.method == 'POST':
        # on récupère les entrées du formulaire
        date_debut = request.form.get('date_debut')
        date_fin = request.form.get('date_fin')
        capteur = request.form.get('capteur')

        # si la date de fin n'est pas renseignée
        if len(date_fin) < 1:
            # ni la date de début
            if len(date_debut) < 1:
                # alors on retourne les valeurs courantes de la station
                from datetime import datetime as dt
                utc_timestamp = dt.strftime(dt.now(), "%d-%m-%Y à %H:%M:%S") # la date courante
                value = get_current_values_co2(capteur)
                return render_template('index.html', title='Accueil', email=current_user.email, utc_timestamp=utc_timestamp, value=value)
            # sinon on retourne les valeurs correspondantes pour ce jour
            else:
                x, y = get_single_day(capteur, date_debut)
        else:
            # si les deux dates sont renseignées, on retourne les valeurs correspondantes à cette période
            x, y = get_range_data(capteur, date_debut, date_fin)

        # on génère les graphiques associés à chaque indicateur
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
                               value=''
                               )

    return render_template('index.html', title='Accueil', email=current_user.email, value='')
