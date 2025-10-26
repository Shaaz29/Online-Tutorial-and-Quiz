from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser non-interactively'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin123'
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully!'))
            self.stdout.write(self.style.WARNING(f'Username: {username}'))
            self.stdout.write(self.style.WARNING(f'Password: {password}'))
            self.stdout.write(self.style.ERROR('CHANGE THIS PASSWORD IMMEDIATELY!'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))

