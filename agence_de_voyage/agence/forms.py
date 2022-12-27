from django import forms

from gestionagence.models import Gestionagence 
# # from .models import agence
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model 

# User = get_user_model() 
# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = {'first_name','last_name','email','password1','password2'}
        
        
    


class UserRegisterForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length = 30)
    email = forms.EmailField()
    password1 = forms.CharField(max_length = 30)
    password2 = forms.CharField(max_length = 30)
    
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(max_length = 50)

class reserveForm(forms.Form):
    depart = forms.ChoiceField()
    destination = forms.ChoiceField()
    datedepart = forms.DateField()
    quantite = forms.IntegerField()


class GestionagenceCreate(forms.ModelForm):
    
    class Meta:
        model = Gestionagence
        fields = '__all__'