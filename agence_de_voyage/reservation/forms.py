from django import forms
from .models import ReservationForm

class ReservationCreate(forms.ModelForm):
    
    class Meta:
        model = ReservationForm
        fields = '__all__'


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

class ReservationForm(forms.Form):
    depart = forms.ChoiceField(label="lieu de depart",choices=departs )
    destination = forms.ChoiceField(label="lieu de destination",choices=arriver)
    datedepart = forms.DateField(label = "date de depart" )
    qte = forms.IntegerField(label = "nombre de place")