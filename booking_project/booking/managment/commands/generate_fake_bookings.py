import random
from django.core.managment.base import BaseCommand
from faker import Faker 
from booking.models import booking

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake booked spots for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake bookings to generate')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for _ in range(count):
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            date = fake.date_between('-30d', '30d')
            time = fake.time_object()

            Booking.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
            )

            self.stdout.write(self.style.SUCCESS(f'Fake booking created for {name}'))