from django.db import models
from django.contrib.auth.models import User
# Create your models her


from django import forms

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

class ReservationCreate(models.Model):
    depart = models.CharField(max_length = 30,choices=departs )
    destination = models.CharField(max_length = 30,default="lieu de destination",choices=arriver)
    datedepart = models.DateField()
    qte = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # reservation=(depart, destination, datedepart, qte)

    