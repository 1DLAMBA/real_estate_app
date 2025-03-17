from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    help = 'Seed the database with sample users'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            User.objects.create_superuser(username="admin", email="admin@example.com", password="password123")
            User.objects.create_user(username="john_doe", email="john@example.com", password="password123")
            User.objects.create_user(username="jane_doe", email="jane@example.com", password="password123")
            self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
        else:
            self.stdout.write(self.style.WARNING('Users already exist, skipping seed.'))
