from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BookingForm
from .models import Booking

def booking_list(request):
    """View to display all bookings."""
    bookings = Booking.objects.all()
    return render(request, 'booking_app/booking_list.html', {'bookings': bookings})

def book_slot(request):
    """View to create a new booking."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_app/book_slot.html', {'form': form})

def get_booked_slots(request):
    """View to return all booked slots in JSON format."""
    booked_slots = Booking.objects.all().values('id', 'title', 'start', 'end')
    return JsonResponse(list(booked_slots), safe=False)

# views.py

def calendar_view(request):
    booked_days = [...] # fetch this from your database or wherever you store booked days
    days_range = range(1, 32)  # For October as an example
    context = {
        'booked_days': booked_days,
        'days_range': days_range
    }
    return render(request, 'booking_app/calendar.html', context)
