# booking/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import BookingForm

def index(request):
    form = BookingForm()
    return render(request, 'booking/index.html', {'form': form})

def submit_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return JsonResponse({'status': 'success', 'message': 'Booking received successfully'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
