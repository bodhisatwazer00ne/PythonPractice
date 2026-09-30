import os
import requests
import pandas as pd


API_URL = "https://api.weatherbit.io/v2.0/current"

API_KEY = os.getenv("WEATHERBIT_API_KEY")

params = {
    "city": "Pune",
    "country": "IN",
    "key": API_KEY
}


try:
    response = requests.get(
        API_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    rows = []

    for weather in data["data"]:
        rows.append({
            "City": weather.get("city_name"),
            "Country": weather.get("country_code"),
            "Temperature": weather.get("temp"),
            "Humidity": weather.get("rh"),
            "Wind Speed": weather.get("wind_spd"),
            "Weather": weather.get("weather", {}).get("description")
        })

    df = pd.DataFrame(rows)

    df.to_excel(
        "weather.xlsx",
        index=False
    )

    print("Excel file created successfully.")

except requests.RequestException as e:
    print(f"API request failed: {e}")

except (KeyError, TypeError) as e:
    print(f"Unexpected API response: {e}")