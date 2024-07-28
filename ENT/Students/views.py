from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
# Class qui gère l'affichage des cours de l'étudiants
class CourseList(APIView):
    def get(self, request):
        user = request.user # récupère les informations de l'user qui fait la requete
        print(user)
        try:
            students = Students.objects.get(id=user.id)
            course = students.courses.all()
            
            # Sérializers les donnés du cours
            print(course)
            course_serialize = CourseSerializers(course, many=True)
            print(course_serialize.data)
            
            return Response (course_serialize.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)