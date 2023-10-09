# booking_project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking_app.urls')),
    path('', include('booking_app.urls')),  # Add this line for an empty path redirect
]

