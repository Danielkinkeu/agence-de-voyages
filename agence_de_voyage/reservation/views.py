from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import messages
from reservation.forms import *


# Create your views here.
def reserver_form(request):
    upload = ReservationCreate()
    if request.method == 'POST':
        upload = ReservationForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save() 
            return render(request, 'reservation_list.html',)
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url: 'reservation'}}">Reload</a> """)
    else:
        return render (request, 'reserver.html', {'ReservationForm': upload})
    
def liste(request):
    return render(request, 'reservation_list.html')