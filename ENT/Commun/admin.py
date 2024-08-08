from django.contrib import admin
from Commun.models import *

class EventAdmin(admin.ModelAdmin):
    model = Events
    list_display = ['id', 'name', 'description', 'start', 'end']
    
class DocumentsAdmin(admin.ModelAdmin):
    model = Documents
    list_display = ['id', 'name', 'link']
    
class ModulesAdmin(admin.ModelAdmin):
    model = Modules
    list_display = ['id','name', 'duration', 'credit']
       
class ForumInline(admin.TabularInline):
    model = ForumContent
    
class ForumAdmin(admin.ModelAdmin):
    inlines = [ForumInline]
    list_display = ['id', 'description', 'create_date', 'modules', 'creator']
        

 
# Register your models here.
admin.site.register(Modules, ModulesAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Events, EventAdmin)
admin.site.register(Forum, ForumAdmin)
