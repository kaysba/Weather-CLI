import os
import requests
from dotenv import load_dotenv

def get_data(city, lang):
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang={lang}"

    response = requests.get(url)
    data = response.json()
    return data