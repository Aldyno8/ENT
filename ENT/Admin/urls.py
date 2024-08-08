from django.urls import path
from .views import *

urlpatterns = [
    path('User/',StudentsList.as_view(), name='Students'),
    path('Prof/', ProfList.as_view(), name='Prof')
]
