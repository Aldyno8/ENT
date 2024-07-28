from django.contrib import admin
from .models import *

# Register your models here.
class ProfAdmin(admin.ModelAdmin):
    model = Professor
    list_display = ['Speciality']
    
admin.site.register(Professor, ProfAdmin)