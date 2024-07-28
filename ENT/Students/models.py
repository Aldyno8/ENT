from django.db import models
from django.contrib.auth.models import User
from Professor.models import Professor as Prof
niveau_choice = [('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3')]
parcours_choice = [('RSI', 'RSI'), ('IDEV', 'IDEV')]

# Create your models here.
# models qui gère les étudiants
class Students(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    Pseudo = models.CharField(max_length=20, null=True)
    Niveau = models.CharField(max_length=3, choices=niveau_choice, default= 'L1')
    Parcours = models.CharField(max_length=5, choices=parcours_choice, default= 'IDEV')
    Age = models.IntegerField()
    Birth =  models.DateField()
    Inscription = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Pseudo
    
# models qui gère les cours
class Modules(models.Model):
    Name = models.CharField(max_length=30)
    Professor = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True, related_name='modules')
    Duration = models.IntegerField()
    Credit = models.IntegerField()
    Students = models.ManyToManyField(Students, blank=True, related_name='modules')
    
    def __str__(self):
        return self.Name
   
# models qui gère les Documents 
class Documents(models.Model):
    Modules = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='contents', null=True)
    Name = models.CharField(max_length=50)
    Link = models.FileField(upload_to='Documents/')
    
    def __str__(self):
        return self.Name
    
# models qui gère les évents
class Events(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    add_date = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Students, related_name='events')
    
    def __str__(self):
        return self.Name
    