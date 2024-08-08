from django.db import models
from Authentication.models import UserModels
niveau_choice = [('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3')]
parcours_choice = [('RSI', 'RSI'), ('IDEV', 'IDEV')]

# Create your models here.
# models qui gère les étudiants
class Students(models.Model):
    User = models.OneToOneField(UserModels, on_delete=models.CASCADE, related_name='user')
    Pseudo = models.CharField(max_length=20, null=True)
    Niveau = models.CharField(max_length=3, choices=niveau_choice, default= 'L1')
    Parcours = models.CharField(max_length=5, choices=parcours_choice, default= 'IDEV')
    Age = models.IntegerField()
    Birth =  models.DateField()
    Inscription = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Pseudo
