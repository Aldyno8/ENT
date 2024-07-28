from django.urls import path
from .views import *

urlpatterns = [
  path('course/', ModulesList.as_view(), name='Course'),
  path('content/<int:id>/', ModulesContent.as_view(), name='content')
]
