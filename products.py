import csv
from faker import Faker
import random
import string

# Initialize Faker
fake = Faker()

def generate_product_code(length=6):
    """Generate a random alphanumeric product code."""
    prefix = 'PR'
    characters = string.ascii_uppercase + string.digits
    return prefix + ''.join(random.choices(characters, k=length))

def generate_fake_beverage_products(num_products):
    beverages = ['Coffee', 'Tea', 'Soda', 'Juice', 'Energy Drink', 'Water', 'Smoothie', 'Milkshake']
    products = []
    for _ in range(num_products):
        beverage = random.choice(beverages)
        product_name = fake.word().capitalize() + ' ' + beverage
        if beverage in ['Coffee', 'Tea']:
            category = 'Hot Beverage'
        elif beverage in ['Soda', 'Juice', 'Energy Drink', 'Water', 'Smoothie', 'Milkshake']:
            category = 'Cold Beverage'
        product_code = generate_product_code()
        products.append({
            'product_code': product_code,
            'product_name': product_name,
            'product_category': category,
        })
    return products

num_products = 200
fake_beverage_products = generate_fake_beverage_products(num_products)

# Define CSV file path
csv_file = 'db/products.csv'

# Write data to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fake_beverage_products[0].keys())
    writer.writeheader()
    for product in fake_beverage_products:
        writer.writerow(product)

print(f"Fake beverage product data has been saved to {csv_file}.")