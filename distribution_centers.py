import csv
import random
import string
from faker import Faker
import random_address

# Initialize Faker
fake = Faker('en-CA')

# Initialize random address
radd = random_address.real_random_address_by_state('BC')

# Fake company name

def generate_code():
    """Generate a random alphanumeric code."""
    prefix = 'DC'
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

def generate_fake_distribution_centers(num_centers):
    centers = []
    for i in range(num_centers):
        # Reverse geocode to get the address from coordinates
        
        name = f"Distribution Center {i + 1}"
        manager_name = fake.name()
        address_details = radd
        code = generate_code()
        centers.append({
            'code': code,
            'name': name,
            'manager': manager_name,
            'address': address_details['address1'],
            'city': address_details['city'],
            'country': address_details['country'],
            'neighborhood': address_details['neighborhood'],
            'postal_code': address_details['postal_code']
        })
    return centers

num_centers = 3
fake_distribution_centers = generate_fake_distribution_centers(num_centers)

# Define CSV file path
csv_file = 'db/distribution_centers.csv'

# Write data to CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fake_distribution_centers[0].keys())
    writer.writeheader()
    for center in fake_distribution_centers:
        writer.writerow(center)

print(f"Fake distribution center data has been saved to {csv_file}.")
