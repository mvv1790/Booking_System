from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from .views import book_slot, booking_list, calendar_view, get_booked_slots

urlpatterns = [
    path('book_slot/', book_slot, name='book_slot'),
    path('booking_list/', booking_list, name='booking_list'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('get_booked_slots/', get_booked_slots, name='get_booked_slots'),
    path('', RedirectView.as_view(url='/calendar/'), name='index_redirect'),
    path('get_booked_slots/', views.get_booked_slots, name='get_booked_slots'),
]
