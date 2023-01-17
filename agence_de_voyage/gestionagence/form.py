from django import forms
from .models import Gestionagence, Bus, Voyage, Quartier, Ville

class GestionagenceCreate(forms.ModelForm):
    
    class Meta:
        model = Gestionagence
        fields = '__all__'
        

class BusCreate(forms.ModelForm):
    
    class Meta:
        model = Bus
        fields = '__all__'
        
class VoyageCreate(forms.ModelForm):
    
    class Meta:
        model = Voyage
        fields = '__all__'        
        

class QuartierCreate(forms.ModelForm):
    
    class Meta:
        model = Quartier
        fields = '__all__'   
        

class VilleCreate(forms.ModelForm):
    
    class Meta:
        model = Ville
        fields = '__all__'             