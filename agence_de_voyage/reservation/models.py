from django.db import models

# Create your models here.
   

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

class ReservationForm(models.Model):
    depart = models.CharField(max_length = 30,default="lieu de depart",choices=departs )
    destination = models.CharField(max_length = 30,default="lieu de destination",choices=arriver)
    datedepart = models.DateField(default = "date de depart")
    qte = models.IntegerField(default = "nombre de place")
    
    def __str__(self):
        return self.depart
    