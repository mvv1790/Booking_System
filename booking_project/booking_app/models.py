from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

