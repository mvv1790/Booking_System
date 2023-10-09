from django.db import models

# Create your models here.
from django.db import models 

class Booking(models.Model):
    name = models.CharField(max_lenght=1000)
    date = models.Date()
    time = models..TimeField()

from django import froms
from .models import Booking

class BookingForm(froms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'band name', 'date', 'time']