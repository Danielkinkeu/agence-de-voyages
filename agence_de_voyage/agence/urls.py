from django import views
from django.urls import path,include

from gestionagence.views import update, delete
from .views import *
from . import views 

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('reservations/', reservations, name="reservations"),
    path('visiter/', visiter, name="visiter"),
    path('visiter/reservations', reservations, name="reservations"),
    path('upload/', views.upload, name='upload-agence'),
    path('index/upload/', views.upload, name='upload-agence'),
    path('upload/<int:gestionagence_id>', update),
    path('delete/<int:gestionagence_id>', delete),
    path('update/<int:gestionagence_id>', update), 

]  