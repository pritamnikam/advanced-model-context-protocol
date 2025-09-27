# Contents of mcp_client.py

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = os.getenv("API_URL")

def get_weather(city):
    """Fetch weather data for a given city."""
    response = requests.get(f"{API_URL}/weather?city={city}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data"}

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    print(weather_data)

if __name__ == "__main__":
    main()