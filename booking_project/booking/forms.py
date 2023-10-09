from django import froms
from .models import Booking

class BookingForm(froms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'band name', 'date', 'time']