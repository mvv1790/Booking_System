from django.db import models

# Create your models here.
from django.db import models 

class Booking(models.Model):
    name = models.CharField(max_lenght=1000)
    date = models.Date()
    time = models..TimeField()