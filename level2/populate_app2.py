import os
import django
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level2.settings')
django.setup()

from app2.models import User

fakegen = Faker()

def populate(N=6):
    for _ in range(N):
        # Generate fake user data
        f_name = fakegen.first_name()
        l_name = fakegen.last_name()
        email = fakegen.email()
        
        # Create or get user with fake data
        User.objects.get_or_create(
            f_name=f_name,
            l_name=l_name,
            email=email
        )
    print(f"{N} users have been created.")

if __name__ == '__main__':
    populate()
