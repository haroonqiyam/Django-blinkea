from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

try:
    superuser = User.objects.create_superuser(
        username='admin',
        email='admin@blinkea.com',
        password='admin123'  # You should change this password
    )
    print('Superuser created successfully!')
except IntegrityError:
    print('Superuser already exists.')
