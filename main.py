from business import *

city = ["Mérignac","Bayonne"]

data = getTempByCity(city)

for city in data:
    print(city["city"], ':' , city["days"])