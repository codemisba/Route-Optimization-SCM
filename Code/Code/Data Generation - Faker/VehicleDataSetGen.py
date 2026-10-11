import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

vehicle_types = ['Delivery Van', 'Bike', 'Mini Truck','Cargo Truck']
fuel_types = ['Diesel', 'Petrol', 'Electric', 'CNG']
availability_status = ['Available', 'In Transit', 'Under Maintenance']

def generate_vehicle_data(n=100):
    vehicles = []

    for i in range(1, n + 1):
        vehicle = {
            'VehicleID': f'VEH{i:04d}',
            'VehicleType': (v_type := random.choice(vehicle_types)),
            'RegistrationNumber': fake.unique.bothify(text='??##??####'),
            'CapacityKg': random.randint(50, 1000) if v_type != 'Bike' else random.randint(20, 50),
            'CurrentLocation': fake.city(),
            'AvailabilityStatus': (status := random.choice(availability_status)),
            'AssignedRouteID': f'RT{random.randint(100, 999)}' if status == 'In Transit' else '',
            'LastMaintenanceDate': (datetime.now() - timedelta(days=random.randint(10, 180))).strftime('%Y-%m-%d'),
            'FuelType': random.choice(fuel_types),
            'GPSEnabled': random.choice(['Yes', 'No'])
        }
        vehicles.append(vehicle)
    
    return vehicles

# Generate vehicle data
vehicle_data = generate_vehicle_data(100)

# Create DataFrame
df = pd.DataFrame(vehicle_data)

# Save to CSV
df.to_csv('../Datasets/Raw/vehicle_data.csv', index=False)

print("Vehicle data saved to 'vehicle_data.csv'")
