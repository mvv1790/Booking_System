# booking_app/urls.py

from django.urls import path
from .views import book_slot_view, booking_list_view, calendar_view
from .views import calendar_view

urlpatterns = [
    path('book_slot/', book_slot_view, name='book_slot'),
    path('booking_list/', booking_list_view, name='booking_list'),
    path('calendar/', calendar_view, name='calendar'),
    path('get_booked_slots/', get_booked_slots, name='get_booked_slots'),
]
