from dotenv import load_dotenv
import os

load_dotenv()

def getWeatherApiKey():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    return api_key