import requests

URL_API = "https://airqino-api.magentalab.it/"


def get_range_data(capteur: str, date_debut: str, date_fin: str) -> tuple[list, dict[str, list]]:
    ''' fournit les données nécessaires pour générer les graphiques liés aux indicateurs de la qualité de l'air
    '''
    # Soit le endpoint de l'API permettant de récupérer les données d'une station
    url = URL_API + f"getRange/{capteur}/{date_debut}/{date_fin}"

    # on effectue une requête de type get sur l'API et on récupère la réponse
    reponse = requests.get(url, timeout=60).json()

    # liste des valeurs de chaque indicateur sur la période donnée
    AUX1_list = []
    AUX2_list = []
    AUX3_list = []
    CO_list = []
    NO2_list = []
    O3_list = []
    PM10_list = []
    PM2_5_list = []
    RH_list = []
    T_list = []
    Temp_int_list = []
    utc_timestamp = []
    indexes = []
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
        indexes.append(i)

    x = utc_timestamp
    y = {'AUX1': AUX1_list, 'AUX2': AUX2_list, 'AUX3': AUX3_list, 'CO': CO_list, 'NO2': NO2_list,
         'O3': O3_list, 'PM10': PM10_list, 'PM2_5': PM2_5_list, 'RH': RH_list, 'T': T_list, 'Temp_int': Temp_int_list}
    print("créée kohfif ")
    return x, y
    # return (utc_timestamp, AUX1_list)
