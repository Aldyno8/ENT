from django.contrib import admin
from Commun.models import *

class EventAdmin(admin.ModelAdmin):
    model = Events
    list_display = ['id', 'Name', 'Description', 'start', 'end']
    
class DocumentsAdmin(admin.ModelAdmin):
    model = Documents
    list_display = ['id', 'Name', 'Link']
    
class ModulesAdmin(admin.ModelAdmin):
    model = Modules
    list_display = ['id','Name', 'Duration', 'Credit']
    

# Register your models here.
admin.site.register(Modules, ModulesAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Events, EventAdmin)