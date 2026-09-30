import os
import requests
import pandas as pd


# ==========================================
# 1. API CONFIGURATION
# ==========================================

API_URL = "https://api.weatherbit.io/v2.0/current"

API_KEY = os.getenv("WEATHERBIT_API_KEY")

if not API_KEY:
    raise ValueError("WEATHERBIT_API_KEY environment variable is not set.")


params = {
    "city": "Pune",
    "country": "IN",
    "key": API_KEY,
    "units": "M"
}


# ==========================================
# 2. GET DATA FROM API
# ==========================================

try:
    response = requests.get(
        API_URL,
        params=params,
        timeout=10
    )

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Convert JSON response into Python dictionary
    data = response.json()

except requests.RequestException as e:
    print(f"API request failed: {e}")
    exit()


# ==========================================
# 3. EXTRACT DATA
# ==========================================

try:
    weather_data = data["data"]

except (KeyError, TypeError):
    print("Unexpected API response format.")
    exit()


# ==========================================
# 4. CONVERT API DATA INTO ROWS
# ==========================================

rows = []

for weather in weather_data:

    rows.append({
        "City": weather.get("city_name"),
        "Country": weather.get("country_code"),
        "Temperature (°C)": weather.get("temp"),
        "Feels Like (°C)": weather.get("app_temp"),
        "Humidity (%)": weather.get("rh"),
        "Wind Speed (m/s)": weather.get("wind_spd"),
        "Pressure (mb)": weather.get("pres"),
        "Visibility (km)": weather.get("vis"),
        "Weather": weather.get("weather", {}).get("description")
    })


# ==========================================
# 5. CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(rows)


# ==========================================
# 6. EXPORT TO EXCEL
# ==========================================

output_file = "weather_data.xlsx"

try:

    df.to_excel(
        output_file,
        index=False
    )

    print(f"Excel file created successfully: {output_file}")

except Exception as e:
    print(f"Failed to create Excel file: {e}")