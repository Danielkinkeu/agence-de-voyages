from django import forms
from .models import Gestionagence

class GestionagenceCreate(forms.ModelForm):
    
    class Meta:
        model = Gestionagence
        fields = '__all__'