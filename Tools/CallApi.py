import requests
from Tools.KeySender import getWeatherApiKey

def call_api(methode, url, params):
    params["appid"] = getWeatherApiKey()

    try:
        response = requests.request(
            methode,
            url,
            params=params
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print("Erreur lors de l'appel API :", e)
        return {None, "here"}