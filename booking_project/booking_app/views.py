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

def calendar_view(request):
    """View to display the calendar."""
    return render(request, 'booking_app/calendar.html')
