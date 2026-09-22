from Tools.CallApi import call_api
from Tools.Methode import getDailyTemperatures

baseUrl = "http://api.openweathermap.org/data/2.5"

def getTempByCity(city=[]):
    result = []

    for i in city:
        params = {
            "q": f"{i},FR",
            "units": "metric"
        }

        data = call_api(
            "GET",
            f"{baseUrl}/forecast",
            params
        )

        temp = []

        for forecast in data["list"]:
            temp.append([
                forecast["dt_txt"],
                forecast["main"]["temp"]
            ])

        dataCity = getDailyTemperatures(temp)

        dataCity.pop()

        result.append({
            "city": i,
            "days": dataCity
        })

    return result
