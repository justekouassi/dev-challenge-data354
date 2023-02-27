import requests

url_get_stations = "https://airqino-api.magentalab.it/getStations/AQ54"

reponse = requests.get(url_get_stations, timeout=60).json()
print(reponse)
