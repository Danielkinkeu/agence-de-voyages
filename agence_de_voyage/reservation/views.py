from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import messages
from reservation.forms import *
from .models import *
from django.contrib.auth.models import User


# Create your views here.
def reserver_form(request):
    upload = ReservationForm()
    user=request.user
    if request.method == 'POST':
        upload = ReservationForm(request.POST)
        reservationcreate=ReservationCreate()
        if upload.is_valid():
            reservationcreate.destination = upload.cleaned_data['destination']
            reservationcreate.depart = upload.cleaned_data['depart']
            reservationcreate.datedepart = upload.cleaned_data['datedepart']
            reservationcreate.qte = upload.cleaned_data['qte']
            reservationcreate.user = user
            reservationcreate.save()
            print(ReservationCreate.depart)
            reservations=ReservationCreate.objects.filter(user=user)
            return render(request, 'reservation_list.html',{'reservations':reservations})
        else:
            return render(request, 'reserver.html',{'upload':upload})
    else:
        return render (request, 'reserver.html', {'upload': upload})
    

def liste(request):
    user=request.user
    reservations=ReservationCreate.objects.filter(user=user)
    return render(request, 'reservation_list.html', {'reservations':reservations})
  
def deleteR(request, reservation_id):
    id = int(reservation_id)
    # try:
    #     reservation_shelf = ReservationCreate.objects.get(id = reservation_id)
    # except ReservationCreate.DoesNotExist:
    #     return redirect('liste')
    # reservation_shelf.delete()
    # return redirect('liste')   
    reservation = ReservationCreate.objects.get(id=id)
    if reservation is not None:
        reservation.delete()
    return redirect('liste')    
