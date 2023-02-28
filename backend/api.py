import requests

URL_API = "https://airqino-api.magentalab.it/"


def get_range_data(capteur: str, date_debut: str, date_fin: str) -> tuple[list, list]:
    url = URL_API + f"getRange/{capteur}/{date_debut}/{date_fin}"

    reponse = requests.get(url, timeout=60).json()

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
        indexes.append(i)

    return (indexes, AUX1_list)
