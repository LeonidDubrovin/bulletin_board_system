from django.test import Client
import random
import os
import requests
from faker import Faker
from django.test.utils import setup_test_environment
import django
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbs.settings')
# setup_test_environment()
django.setup()

# if not settings.configured:
#     django.setup()

fake = Faker(locale="ru_RU")


def generate_ad():
    num = 10
    c = Client()
    logged_in = c.login(username='Lenz007', password='12345678qw')
    for i in range(1, num + 1):
        ad_data = {
            "title": fake.company(),
            "price": random.randint(10, 100),
            "description": fake.text(),
            "phone": fake.phone_number(),
            "video": '',
            "file_count": 0,
            "category": fake.profile()["job"],
            "city": fake.city(),
            "region": fake.administrative_unit(),
        }

        response = c.post("/post-ads/", ad_data)
        print(i, response.status_code)


if __name__ == "__main__":
    generate_ad()
