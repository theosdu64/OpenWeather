import requests

def call_api(methode, url):
    try:
        response = requests.request(methode, url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print("Erreur lors de l'appel API :", e)
        return None