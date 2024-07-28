from django.urls import path
from .views import *


urlpatterns = [
    path('ModulesList/',ModuleListView.as_view(), name='Modules'),
    path('content/<int:id>/', ModulesContent.as_view(), name='Content'),
    
]
