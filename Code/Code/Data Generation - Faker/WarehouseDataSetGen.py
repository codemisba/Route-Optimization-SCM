import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_warehouse_data(n=50):
    warehouses = []

    for i in range(1, n + 1):
        city = fake.city()
        state = fake.state()
        lat = round(fake.latitude(), 6)
        lon = round(fake.longitude(), 6)

        warehouse = {
            'WarehouseID': f'WH{i:03d}',
            'WarehouseName': f'{fake.company()} Warehouse',
            'City': city,
            'State': state,
            'Latitude': lat,
            'Longitude': lon,
            'StorageCapacityTons': (capacity := random.randint(100, 5000)),
            'CurrentUtilizationPercent': (utilization := round(random.uniform(20, 100), 2)),
            'ManagerName': fake.name(),
            'ContactNumber': fake.phone_number(),
            'OperatingHours': '08:00 - 20:00',
            'IsOperational': 'Yes' if utilization < 95 else 'No'
        }

        warehouses.append(warehouse)
    
    return warehouses

# Generate data
warehouse_data = generate_warehouse_data(50)

# Create DataFrame
df = pd.DataFrame(warehouse_data)

# Save to CSV
df.to_csv('../Datasets/Raw/warehouse_data.csv', index=False)

print("Warehouse data saved to 'warehouse_data.csv'")
