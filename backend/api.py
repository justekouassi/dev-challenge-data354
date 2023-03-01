''' Module de gestion des requêtes API
'''

import requests

URL_API = "https://airqino-api.magentalab.it/"  # url de l'API


def getResponse(url: str) -> requests.Response:
    ''' retourne la réponse d'une requête de type GET
    '''
    return requests.get(url, timeout=60).json()


def get_raw_data(reponse: requests.Response) -> tuple[list, dict[str, list]]:
    ''' fournit les données d'un capteur à partir de la réponse d'un endpoint donné
    '''
    # listes des valeurs de chaque indicateur sur la période donnée
    AUX1_list = AUX2_list = AUX3_list = CO_list = NO2_list = O3_list = PM10_list = PM2_5_list = RH_list = T_list = Temp_int_list = utc_timestamp = []
    for i in range(len(reponse['raw_data'])):
        AUX1_list.append(reponse['raw_data'][i]['AUX1'])
        AUX2_list.append(reponse['raw_data'][i]['AUX2'])
        AUX3_list.append(reponse['raw_data'][i]['AUX3'])
        CO_list.append(reponse['raw_data'][i]['CO'])
        NO2_list.append(reponse['raw_data'][i]['NO2'])
        O3_list.append(reponse['raw_data'][i]['O3'])
        PM10_list.append(reponse['raw_data'][i]['PM10'])
        PM2_5_list.append(reponse['raw_data'][i]['PM2.5'])
        RH_list.append(reponse['raw_data'][i]['RH'])
        T_list.append(reponse['raw_data'][i]['T'])
        Temp_int_list.append(reponse['raw_data'][i]['Temp. int.'])
        utc_timestamp.append(reponse['raw_data'][i]['utc_timestamp'])

    x = utc_timestamp
    y = {'AUX1': AUX1_list, 'AUX2': AUX2_list, 'AUX3': AUX3_list, 'CO': CO_list, 'NO2': NO2_list,
         'O3': O3_list, 'PM10': PM10_list, 'PM2_5': PM2_5_list, 'RH': RH_list, 'T': T_list, 'Temp_int': Temp_int_list}
    return x, y


def get_range_data(capteur: str, date_debut: str, date_fin: str) -> tuple[list, dict[str, list]]:
    ''' fournit la liste des valeurs des indicateurs de la qualité de l'air prises par un capteur et associées à leurs dates d'enregistrement respectives
    '''
    # Soit le endpoint de l'API permettant de récupérer les données d'une station sur une période donnée
    url_get_range = URL_API + f"getRange/{capteur}/{date_debut}/{date_fin}"

    # on effectue une requête de type get sur l'API et on récupère la réponse
    reponse = getResponse(url_get_range)

    return get_raw_data(reponse)


def get_single_day(capteur: str, date: str) -> tuple[list, dict[str, list]]:
    ''' fournit la liste des valeurs des indicateurs de la qualité de l'air prises par un capteur pour un jour donné
    '''
    # Soit le endpoint de l'API permettant de récupérer les données d'une station pour un jour donné
    url_get_single_day = URL_API + f"getSingleDay/{capteur}/{date}"

    # on effectue une requête de type get sur l'API et on récupère la réponse
    reponse = getResponse(url_get_single_day)

    return get_raw_data(reponse)


def get_current_values_co2(capteur: str) -> tuple[str, str]:
    ''' produit les dernières valeurs du CO2 pour une station donnée
    '''
    # Soit le endpoint de l'API permettant de récupérer les dernières valeurs du CO2 d'une station
    url_get_current_values_co2 = URL_API + f"getCurrentValues/{capteur}"

    # on effectue une requête de type get sur l'API et on récupère la réponse
    reponse = getResponse(url_get_current_values_co2)

    # la valeur courante de la quantité de CO2 dans l'air
    value = reponse['values'][0]['value']

    return value
