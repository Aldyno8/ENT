from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserModels
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = UserModels
    list_display = ('username', 'email')
    
admin.site.register(UserModels, UserAdmin)
