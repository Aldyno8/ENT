from django.db import models
from Students.models import Students
from Professor.models import Professor as Prof
from Authentication.models import UserModels

# Create your models here.
# models qui gère les cours   
class Modules(models.Model):
    name = models.CharField(max_length=30)
    professor = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True, related_name='modules')
    duration = models.IntegerField()
    credit = models.IntegerField()
    students = models.ManyToManyField(Students, blank=True, related_name='modules')
    
    def __str__(self):
        return self.name
   
# models qui gère les évents 
class Documents(models.Model):
    modules = models.ForeignKey(Modules, on_delete=models.CASCADE, related_name='contents', null=True)
    name = models.CharField(max_length=50)
    link = models.FileField(upload_to='Documents/')
    
# models qui gère les évents
class Events(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    add_date = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Students, related_name='events')
    
    def __str__(self):
        return self.name

# models qui gère le forum
class Forum(models.Model):
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modules = models.OneToOneField(Modules, on_delete=models.CASCADE, related_name='forum')
    creator = models.ForeignKey(UserModels, on_delete=models.CASCADE, related_name='forum')     
    
    def __str__(self):
        return self.description
    
class ForumContent(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='Thème')
    creator = models.ForeignKey(UserModels, on_delete=models.CASCADE, related_name='creator')
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.content
    