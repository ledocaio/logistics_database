import csv
from faker import Faker
import random
import string

# Initialize Faker
fake = Faker('en_CA')  # 'en_CA' for Canadian English locale

# Define South provinces of Canada
south_provinces = ['Ontario', 'Quebec', 'Nova Scotia', 'New Brunswick', 'Prince Edward Island', 'Newfoundland and Labrador']

def generate_client_code(length=8):
    """Generate a random alphanumeric product code."""
    prefix = 'CL'
    characters = string.ascii_uppercase + string.digits
    return prefix + ''.join(random.choices(characters, k=length))

def generate_fake_clients(num_clients):
    clients = []
    for _ in range(num_clients):
        company_code = generate_client_code()
        company_name = (fake.company() +' '+  fake.company_suffix())
        name = fake.name()
        address = fake.street_address()
        city = fake.city()
        province = random.choice(south_provinces)
        postal_code = fake.postcode()
        phone_number = fake.phone_number()
        email = fake.email()
        clients.append({
            'company_code': company_code,
            'company_name':company_name,
            'name': name,
            'address': address,
            'city': city,
            'province': province,
            'postal_code': postal_code,
            'phone_number': phone_number,
            'email': email
        })
    return clients

num_clients = 20000
fake_clients = generate_fake_clients(num_clients)

# Define CSV file path
csv_file = 'db/clients.csv'

# Write data to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fake_clients[0].keys())
    writer.writeheader()
    for client in fake_clients:
        writer.writerow(client)

print(f"Fake client data has been saved to {csv_file}.")
