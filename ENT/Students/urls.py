from django.urls import path
from .views import *

urlpatterns = [
  path('course/', CourseList.as_view(), name='Course')
]
