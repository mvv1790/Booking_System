from django.shortcuts import render

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        return render(request, 'success.html')
    else:
            return render(request, 'form.html')

from django.urls import path
from . import views


urlpatterns = [
    path('', views.submit_form, name='submit_form')
]