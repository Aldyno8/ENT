from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models pour les professeurs
class Professor(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prof')
    Speciality = models.CharField(max_length=100)
    Embauche_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Speciality
    
    
    