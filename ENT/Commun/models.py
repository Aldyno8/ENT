from django.db import models
from Students.models import Students
from Professor.models import Professor as Prof

# Create your models here.
# models qui gère les cours
class Modules(models.Model):
    Name = models.CharField(max_length=30)
    Professor = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True, related_name='modules')
    Duration = models.IntegerField()
    Credit = models.IntegerField()
    Students = models.ManyToManyField(Students, blank=True, related_name='modules')
    
    def __str__(self):
        return self.Name
    
class Documents(models.Model):
    Modules = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='contents', null=True)
    Name = models.CharField(max_length=50)
    Link = models.FileField(upload_to='Documents/')
    
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
    