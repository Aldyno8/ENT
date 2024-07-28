from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Authentication.urls')),
    path('students/', include('Students.urls')),
    path('professor/', include('Professor.urls'))
]
