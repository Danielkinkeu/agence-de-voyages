from django.urls import path
from app_auth.views import *

urlpatterns = [
    path('login_form',login_form, name='login_form'),
    path('register_form',register_form, name='register_form'),
    path('logout',logout_form, name='logout')
]
