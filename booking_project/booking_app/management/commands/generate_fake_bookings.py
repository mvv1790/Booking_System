# booking_app/management/commands/generate_fake_bookings.py

from django.core.management.base import BaseCommand
from booking_app.models import Booking  # Update this import statement
from faker import Faker
import random
import datetime

class Command(BaseCommand):
    help = 'Generate fake booked spots for testing purposes'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of fake bookings to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        for _ in range(count):
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            date = fake.date_between(start_date='-30d', end_date='today')
            time = datetime.time(random.randint(9, 18), 0)

            Booking.objects.create(name=name, email=email, phone=phone, date=date, time=time)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} fake bookings'))
