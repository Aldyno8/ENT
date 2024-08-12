from django.urls import path
from .views import *

urlpatterns = [
    path('Student/',StudentsList.as_view(), name='Students'),
    path('Prof/', ProfList.as_view(), name='Prof'),
    path('CreateEvent/', CreateEvent.as_view(), name='Event'),
    path('CreateModule/', CreateModule.as_view(), name='Modules')
]
