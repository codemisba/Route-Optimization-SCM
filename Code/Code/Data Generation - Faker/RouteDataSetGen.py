import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_route_data(n=100, warehouse_ids=None):
    routes = []

    if warehouse_ids is None:
        warehouse_ids = [f'WH{i:03d}' for i in range(1, 51)]

    for i in range(1, n + 1):
        source = random.choice(warehouse_ids)
        destination = fake.city()
        distance_km = random.randint(20, 1500)
        avg_speed = random.uniform(40, 80)
        travel_time = round(distance_km / avg_speed, 2)

        route = {
            'RouteID': f'RT{i:04d}',
            'SourceWarehouseID': source,
            'DestinationCity': destination,
            'DistanceKm': distance_km,
            'EstimatedTravelTimeHrs': travel_time,
            'RoutePriority': random.choice(['High', 'Medium', 'Low']),
            'IsActive': random.choice(['Yes', 'No'])
        }
        routes.append(route)

    return routes

# Generate and save
routes = generate_route_data()
df_routes = pd.DataFrame(routes)
df_routes.to_csv('../Datasets/Raw/route_data.csv', index=False)
print("Route data saved to 'route_data.csv'")
