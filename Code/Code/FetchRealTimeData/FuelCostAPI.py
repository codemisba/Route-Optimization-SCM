import requests
import pandas as pd

"""
​Integrating live fuel cost data into your 
Supply Chain Management Dynamic Route Optimization project 
is essential for accurate cost estimation and efficient route planning. The Gasoline Prices API from Zyla Labs provides real-time fuel prices across various locations, which can be leveraged for this purpose
"""

# Replace 'api_key' with the actual API key
# for the Zyla Labs API
# API key for authentication
api_key = 'api_key'

headers = {
    'Authorization': f'Bearer {api_key}'
}

# Define the API endpoint
api_url = 'https://zylalabs.com/api/3927/gasoline+prices+api/4649/fuel+costs'
                                                                            

# Function to fetch fuel prices
def fetch_fuel_prices():
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Retrieve data
fuel_data = fetch_fuel_prices()

# Process and display data if retrieval was successful
if fuel_data:
    # Convert the data into DataFrame for analysis
    df = pd.DataFrame(fuel_data)
    print(df.head())
else:
    print("Failed to retrieve fuel price data.")

# Save the DataFrame to a CSV file  
if fuel_data:
    df.to_csv('../Datasets/Raw/fuel_prices.csv', index=False)
    print("Fuel prices data saved to 'fuel_prices.csv'")  