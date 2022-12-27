from django.urls import path

from agence.views import home, login, register
# from .views import *
from gestionagence import views

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('index/', views.index, name="index"),
    path('upload/', views.upload, name='upload-agence'),
    path('upload/<int:gestionagence_id>', views.update),
    path('delete/<int:gestionagence_id>', views.delete),
    path('update/<int:gestionagence_id>', views.update), 
    path('index/delete/<int:gestionagence_id>', views.delete),
    path('index/update/<int:gestionagence_id>', views.update), 

]  