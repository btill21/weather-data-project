import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHERSTACK_API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Louisiana"
    
def fetch_data():
    print("Fetching data from Weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Data fetched successfully")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise




def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Louisiana, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Louisiana', 'country': 'United States of America', 'region': 'Louisiana', 'lat': '30.9843', 'lon': '-91.9623', 'timezone_id': 'America/Chicago', 'localtime': '2024-06-10 12:00', 'localtime_epoch': 1717944000, 'utc_offset': '-5.0'}, 'current': {'observation_time': '05:00 PM', 'temperature': 28, 'weather_code': 113, 'weather_icons': ['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'wind_speed': 10, 'wind_degree': 150, 'wind_dir': 'SSE', 'pressure': 1012, 'precip': 0, 'humidity': 60, 'cloudcover': 0, 'feelslike': 30, 'uv_index': 7, 'visibility': 16, 'is_day': 'yes'}}