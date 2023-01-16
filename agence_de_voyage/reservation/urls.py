from django.urls import path
from reservation.views import *

urlpatterns = [
    path('reservation',reserver_form, name='reserver_form'),
    path('liste',liste, name='liste'),
    
   
]
