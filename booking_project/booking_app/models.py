from datetime import datetime

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

    @property
    def title(self):
        return self.name

    @property
    def start(self):
        return f"{self.date}T{self.time}"

    @property
    def end(self):
        
        end_time = (datetime.datetime.combine(self.date, self.time) + datetime.timedelta(hours=1)).time()
        return f"{self.date}T{end_time}"
