import requests
import pandas as pd

"""
Why Weather Data Matters in SCM Dynamic Route Optimization ?

Weather data is crucial for optimizing supply chain routes.
It helps in making informed decisions about delivery routes.
1) Delays due to rain, storms, or fog can impact delivery schedules.

2) Route adjustments are necessary based on real-time conditions.

3) Safety for drivers and cargo improves with weather-aware routing.
"""
def get_live_weather_for_cities(cities):
    results = []

    # Predefined latitude and longitude for Indian cities
    city_coords = {
        "Delhi": (28.6139, 77.2090),
        "Mumbai": (19.0760, 72.8777),
        "Bangalore": (12.9716, 77.5946),
        "Chennai": (13.0827, 80.2707),
        "Kolkata": (22.5726, 88.3639),
        "Hyderabad": (17.3850, 78.4867),
        "Ahmedabad": (23.0225, 72.5714),
        "Pune": (18.5204, 73.8567),
        "Jaipur": (26.9124, 75.7873),
        "Lucknow": (26.8467, 80.9462)
    }

    for city in cities:
        if city not in city_coords:
            print(f"Coordinates not found for {city}")
            continue

        lat, lon = city_coords[city]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

        try:
            response = requests.get(url)
            response.raise_for_status()
            weather = response.json()["current_weather"]

            results.append({
                "City": city,
                "Latitude": lat,
                "Longitude": lon,
                "Temperature (°C)": weather["temperature"],
                "Wind Speed (km/h)": weather["windspeed"],
                "Weather Code": weather["weathercode"],
                "Time": weather["time"]
            })

        except Exception as e:
            print(f"Error fetching data for {city}: {e}")

    df = pd.DataFrame(results)
    print(df)
    return df

# Get live weather for major Indian logistics cities
cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad"]
weather_df = get_live_weather_for_cities(cities)

# Save to CSV
weather_df.to_csv("../Datasets/API/live_weather_india.csv", index=False)

print("Weather data saved to 'live_weather_india.csv'")