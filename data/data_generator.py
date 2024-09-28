from faker import Faker
import random

fake = Faker()

def generate_airport_data():
    data = {
        'airport_code': fake.lexify(text='???').upper(),  # Generates a 3-letter IATA code
        'airport_name': fake.company() + ' International Airport',  # Generates a random airport name
        'airport_city': fake.city(),  # Generates a random city name
        'airport_region': fake.state(),  # Generates a random state/region
        'airport_country': fake.country()  # Generates a random country name
    }
    return data