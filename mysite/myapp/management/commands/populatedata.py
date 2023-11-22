
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Person

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start populating data...'))

        # Change the range to the number of fake records you want to create
        for _ in range(10):
            person = Person.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
            )
            self.stdout.write(self.style.SUCCESS(f'Created person: {person}'))

        self.stdout.write(self.style.SUCCESS('Data population complete.'))
