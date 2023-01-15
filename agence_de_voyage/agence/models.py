from django.db import models

# Create your models here.
class UserRegisterform(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length = 30, default = 'Daniel')
    email = models.EmailField(blank=True)
    password1 = models.CharField(max_length = 50)
    password2 = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.email