# booking_app/urls.py

from django.urls import path
from .views import booking_list, book_slot

urlpatterns = [
    path('', booking_list, name='booking_list'),
    path('book_slot/', book_slot, name='book_slot'),
]
