import datetime
from django import forms
from django.contrib.auth.models import User
from gestionagence.models import Gestionagence 
# # from .models import agence
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model 

# User = get_user_model() 
# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = {'first_name','last_name','email','password1','password2'}
        
        
    

# user = User.objects.create_user('daniel','kinkeufranck@gmail.com','kinkeu')
# user.last_name = 'kinkeu'
# user.save()
class UserRegisterForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length = 30)
    email = forms.EmailField()
    password1 = forms.CharField(max_length = 30)
    password2 = forms.CharField(max_length = 30)
    
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(max_length = 50)


departs=[
    ('yaounde','yaounde'),
    ('douala','douala'),
    ('bafoussam','bafoussam'),
    ('dschang','dschang'),
    ('buea','buea'),
]

arriver=[
    ('douala','douala'),
    ('yaounde','yaounde'),
    ('bafoussam','bafoussam'),
    ('dschang','dschang'),
    ('buea','buea'),
]

class reserveForm(forms.Form):
    depart = forms.ChoiceField( choices=departs)
    destination = forms.ChoiceField(choices=arriver)
    datedepart = forms.DateField() 
    quantite = forms.IntegerField()




class GestionagenceCreate(forms.ModelForm):
    
    class Meta:
        model = Gestionagence
        fields = '__all__'