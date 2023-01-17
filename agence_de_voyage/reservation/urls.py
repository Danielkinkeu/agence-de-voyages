from django.urls import path
from reservation.views import *

urlpatterns = [
    # path('', homes, name="homes"),
    path('reservation/form',reserver_form, name='reserver_form'),
    path('reservations', liste , name='liste'),
    path('deleteR/<int:reservation_id>', deleteR, name='deleteR'),
    
   
]
