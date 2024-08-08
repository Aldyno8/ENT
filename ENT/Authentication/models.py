from django.db import models
from django.contrib.auth.models import AbstractUser

role_choices = [('Etudiant', 'Etudiant'), ('Professeur', 'Professeur')]

# Create your models here.
# models user personalisé
class UserModels(AbstractUser):
    role = models.CharField(max_length=25, choices=role_choices, default= 'Etudiant')