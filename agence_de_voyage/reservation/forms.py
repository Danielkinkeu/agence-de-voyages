from django import forms

# class ReservationCreate(forms.ModelForm):
#         class Meta:
#          model = ReservationForm
#          fields = '__all__'


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

# class ReservationForm(forms.Form):
#     depart = forms.ChoiceField(label="Lieu de depart",widget=forms.TextInput(attrs={'class': 'form-control'}), choices=departs)
#     destination = forms.ChoiceField(label="lieu de destination",widget=forms.TextInput(attrs={'class': 'form-control'}), choices=arriver)
#     datedepart = forms.DateField(label="Date de depart",widget=forms.DateInput(attrs={'class': 'form-control'}))
#     qte = forms.IntegerField(label="nombre de place",widget=forms.TextInput(attrs={'class': 'form-control'}))


from .models import ReservationCreate

class ReservationForm(forms.ModelForm):
    class Meta:
        model=ReservationCreate
        exclude=("user",)
        widgets={"datedepart":forms.DateInput(attrs={"type":"date",'class': 'form-control'}),
                 
                 "depart":forms.Select(attrs={'class': 'form-control'}),
                 "destination":forms.Select(attrs={'class': 'form-control'}),
                "qte":forms.NumberInput(attrs={'class': 'form-control'})}

    