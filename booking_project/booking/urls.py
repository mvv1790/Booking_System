from django.urls import path
from .views import index, submit_booking

urlpatterns = [
    path ('', index, name='index'),
    path ('submit_booking/', submit_booking, name='submit_booking'),
]