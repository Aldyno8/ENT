from django.contrib import admin
from .models import *

# Register your models here
class StudentsAdmin(admin.ModelAdmin):
    model = Students
    list_display = ['id', 'Niveau', 'Parcours', 'Age', 'Birth', 'Inscription']
    
class ModulesAdmin(admin.ModelAdmin):
    model = Modules
    list_display = ['id','Name', 'Duration', 'Credit']
    
class DocumentsAdmin(admin.ModelAdmin):
    model = Documents
    list_display = ['id', 'Name', 'Link']
    
admin.site.register(Students, StudentsAdmin)
admin.site.register(Modules, ModulesAdmin)
admin.site.register(Documents, DocumentsAdmin)

