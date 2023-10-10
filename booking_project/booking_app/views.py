from datetime import date, timedelta, datetime
from calendar import monthrange
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
    bookings = Booking.objects.all()

    data = [{
        "title": booking.name,
        "start": f"{booking.date}T{booking.time}",
        "end": (datetime.combine(booking.date, booking.time) + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S")
    } for booking in bookings]

    return JsonResponse(data, safe=False)

def calendar_view(request):
    # Let's assume you want to show the current month:
    today = date.today()
    start_month = date(today.year, today.month, 1)
    
    # Handling month overflow for end_month calculation
    _, last_day = monthrange(today.year, today.month)
    end_month = date(today.year, today.month, last_day)

    # Generating days_range for the month
    days_range = [(start_month + timedelta(days=i)).day for i in range((end_month - start_month).days + 1)]

    # Fetch booked names for days from the database:
    bookings = Booking.objects.filter(date__gte=start_month, date__lte=end_month)
    booked_map = {b.date.day: b.name for b in bookings}

    context = {
        'days_range': days_range,
        'booked_map': booked_map,
    }
    return render(request, 'booking_app/calendar.html', context)
