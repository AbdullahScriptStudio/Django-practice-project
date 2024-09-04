import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nora1.settings')


import django
django.setup()

from faker import Faker 
keygen = Faker()
from norasite.models import Product

def populate(N=5):
    
    for i in range(N):
        p = Product.objects.get_or_create(name = keygen.name(), price = 1000, date = keygen.date())
        
    return 

if __name__ == "__main__":
    populate()
    print('process successfully completed')        
