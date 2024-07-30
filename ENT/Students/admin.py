from django.contrib import admin
from .models import *

# Register your models here
class StudentsAdmin(admin.ModelAdmin):
    model = Students
    list_display = ['id', 'Niveau', 'Parcours', 'Age', 'Birth', 'Inscription']
    

admin.site.register(Students, StudentsAdmin)


