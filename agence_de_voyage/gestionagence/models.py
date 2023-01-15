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