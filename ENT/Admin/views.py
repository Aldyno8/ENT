from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Students.models import Students
from Professor.models import Professor
from .serializers import *

# Create your views here.
class StudentsList(APIView):
    def get(self, request):
        try:
            students_list = Students.objects.all()
            students = StudentsSerialiers(students_list, many=True)
            return Response(students.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
class ProfList(APIView):
    def get(self, request):
        try:
            Professor_list = Professor.objects.all()
            Professor = ProfessorSerialiers(Professor_list, many=True)
            return Response(Professor.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            

                
           
        
    