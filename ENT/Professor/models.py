from django.db import models
from Authentication.models import UserModels
# Create your models here.
# models pour les professeurs
class Professor(models.Model):
    User = models.OneToOneField(UserModels, on_delete=models.CASCADE, related_name='prof')
    Speciality = models.CharField(max_length=100)
    Embauche_date = models.DateTimeField(auto_now_add=True)
    
    def str__(self):
        return self.Speciality
    
    
    