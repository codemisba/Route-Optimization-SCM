import pandas as pd
from faker import Faker
import random

fake = Faker()

delivery_slots = ['08:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00', '16:00-18:00']
delivery_frequencies = ['One-time', 'Weekly', 'Bi-weekly', 'Monthly']

def generate_customer_data(n=2000):
    customers = []

    for i in range(1, n + 1):
        lat = round(fake.latitude(), 6)
        lon = round(fake.longitude(), 6)
        full_address = fake.street_address()

        customer = {
            'CustomerID': f'CUST{i:05d}',
            'FullName': fake.name(),
            'StreetAddress': full_address,
            'City': (city := fake.city()),
            'State': (state := fake.state()),
            'ZipCode': fake.zipcode(),
            'Latitude': lat,
            'Longitude': lon,
            'PhoneNumber': fake.phone_number(),
            'Email': fake.email(),
            'PreferredDeliverySlot': random.choice(delivery_slots),
            'DeliveryFrequency': (freq := random.choice(delivery_frequencies)),
            'IsPriorityCustomer': 'Yes' if freq in ['Weekly', 'Bi-weekly'] and random.random() > 0.7 else 'No'
        }

        customers.append(customer)

    return customers

# Generate data
customer_data = generate_customer_data(2000)

# Convert to DataFrame
df_customers = pd.DataFrame(customer_data)

# Save to CSV
df_customers.to_csv('../Datasets/Raw/customer_data.csv', index=False)

print("Customer data saved to 'customer_data.csv'")
