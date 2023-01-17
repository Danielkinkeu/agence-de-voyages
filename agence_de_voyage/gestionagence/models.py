from django.db import models

# Create your models here.
class Gestionagence(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    siege  = models.CharField(max_length = 30, default = 'Yaounde')
    telephone = models.CharField(max_length = 30, default = '678963685')
    description = models.CharField(max_length = 30, default='Description de l agence ')
    
    def __str__(self):
        return self.name
    
    class UserRegisterForm(models.Model):
        firstname = models.CharField(max_length=50)
        lastname = models.CharField(max_length = 30)
        email = models.EmailField()
        password1 = models.CharField(max_length = 30)
        password2 = models.CharField(max_length = 30)
        

class Bus(models.Model):
    idBus = models.CharField(max_length=50)
    typeBus  = models.CharField(max_length = 30, default = 'Yaounde')
    nombrePlace = models.IntegerField()
    nombrePlaceDispo = models.IntegerField()
    
    def __str__(self):
        return self.idBus
    
    
class Voyage(models.Model):
    idVoyage = models.CharField(max_length=50)
    lieuDepart  = models.CharField(max_length = 30, default = 'Yaounde')
    lieuArriver = models.CharField(max_length = 30, default = '678963685')
    heureDepart = models.TimeField()
    heureArriver = models.TimeField()
    
    def __str__(self):
        return self.idVoyage
    
    
class Quartier(models.Model):
    idQuartier = models.CharField(max_length=50)
    nomQuartier  = models.CharField(max_length = 30, default = '')
    
    def __str__(self):
        return self.idQuartier 
    
    
class Ville(models.Model):
    idVille = models.CharField(max_length=50)
    nomVille = models.CharField(max_length = 30, default = '')
    
    def __str__(self):
        return self.idVille           