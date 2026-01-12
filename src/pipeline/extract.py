import requests
import json


def fetch_weather_data(city, api_key):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    response.raise_for_status
    return response.json()
