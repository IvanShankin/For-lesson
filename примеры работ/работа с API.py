import requests

city = input("Введите город: ")

url = f"https://wttr.in/{city}?format=j1"

weather_response = requests.get(url,)
weather = weather_response.json()
current = weather["current_condition"][0]

print(f"Температура: {current['temp_C']} °C")
print(f"Влажность воздуха: {current['humidity']} %")
print(f"Ветер: {current['windspeedKmph']} км/ч")
print(f"атмосферное давление: {current['pressure']} гПа/мбар")





