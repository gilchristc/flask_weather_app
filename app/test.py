import requests
import json

city = "Metro Manila"
country = "PH"

api_key="2508d329aeede27d07b56f3a2e533c1f"


weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=imperial')
weather_data = weather_url.json()

temp = round(weather_data['main']['temp'])
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']



