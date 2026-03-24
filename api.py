import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Nice",
    "appid": os.getenv("API_KEY"),
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()
print(data)