from django.contrib.auth.models import User


username = 'root'
email = 'admin@example.com'
password = 'root'

# Проверка существования пользователя
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created successfully!')
else:
    print(f'Superuser {username} already exists.')
