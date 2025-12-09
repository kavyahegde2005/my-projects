import requests

city_name = "California"

api_key = "7bf94696c65981ce265d1d0afc2f5603"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")  #endpoint for current weather data

print(response.status_code)

if response.status_code == 200:
    result = response.json()
    result = result["main"]["temp"]
    result = result - 273.15
    print(round(result))
