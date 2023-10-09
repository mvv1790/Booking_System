from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_app/booking_list.html', {'bookings': bookings})

def book_slot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_app/book_slot.html', {'form': form})
