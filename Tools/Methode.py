baseUrl = "http://api.openweathermap.org/data/2.5"

def getUniqueday(data):
    day = []

    for i in data:
        date = i[0].split(" ")[0]
        if date not in day:
            day.append(date)

    return day


def groupTemperaturesByDay(dataTxt):
    day = getUniqueday(dataTxt)
    result = []

    for i in day:
        temperatures = []

        for y in dataTxt:
            date_prevision = y[0].split(" ")[0]

            if i == date_prevision:
                temperatures.append(y[1])

        result.append({
            "date": i,
            "temperatures": temperatures
        })

    return result


def minAndMax(data):
    return min(data), max(data)


def getDailyTemperatures(dataFromApi):
    data = groupTemperaturesByDay(dataFromApi)

    for i in data:
        i["min"], i["max"] = minAndMax(i["temperatures"])
        del i["temperatures"]
    return data