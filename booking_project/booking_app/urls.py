# booking_app/urls.py

from django.urls import path
from .views import booking_list, book_slot, get_booked_slots

urlpatterns = [
    path('', booking_list, name='booking_list'),
    path('book_slot/', book_slot, name='book_slot'),
    path('get_booked_slots/', get_booked_slots, name='get_booked_slots')
]