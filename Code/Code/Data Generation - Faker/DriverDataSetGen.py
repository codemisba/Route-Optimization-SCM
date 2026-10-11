import pandas as pd
from faker import Faker
import random

fake = Faker()

vehicle_types = ['Delivery Van', 'Bike', 'Mini Truck', 'Cargo Truck']
employment_statuses = ['Full-Time', 'Part-Time', 'Contract']

def generate_delivery_driver_data(n=10):
    drivers = []
    for _ in range(n):
        driver = {
            'DriverName': fake.name(),
            'LicenseNumber': fake.unique.bothify(text='DL#####??'),
            'PhoneNumber': fake.phone_number(),
            'VehicleType': random.choice(vehicle_types),
            'VehicleRegNumber': fake.unique.bothify(text='??##??####'),
            'DeliveryArea': fake.city(),
            'EmploymentStatus': random.choice(employment_statuses),
            'Company': fake.company()
        }
        drivers.append(driver)
    return drivers

# Generate data
driver_data = generate_delivery_driver_data(10)

# Convert to DataFrame
df = pd.DataFrame(driver_data)

# Save to CSV
df.to_csv('../Datasets/Raw/delivery_driver_data.csv', index=False)

print("Data saved to 'delivery_driver_data.csv'")
