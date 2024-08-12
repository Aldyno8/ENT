from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Students.models import Students
from Professor.models import Professor as prof
from Commun.models import *
from .serializers import *

# Create your views here.
# Liste des étudians
class StudentsList(APIView):
    def get(self, request):
        try:
            students_list = Students.objects.all()
            students = StudentsSerialiers(students_list, many=True)
            return Response(students.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
     
# Liste des prof       
class ProfList(APIView):
    def get(self, request):
        try:
            Professor_list = prof.objects.all()
            Professor = ProfessorSerialiers(Professor_list, many=True)
            return Response(Professor.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# Création d'évenement pour l'EDT
class CreateEvent(APIView):
    def post(seld, request):
        try:
            name = request.data.get('name')
            description = request.data.get('description')
            start = request.data.get('start')
            end = request.data.get('end')
            students = request.data.get('students')
            
            event = Events.objects.create(
                name = name,
                description=description,
                start=start,
                end=end,
                students=students
            )
            
            return Response({"message":"Event crée avec succès"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":str(e)})
          
# Ajout de nouveau modules
class CreateModule(APIView):
    def post(self, request):
        name = request.data.get('name')
        professor = request.data.get('professor')
        duration = request.data.get('duration')
        credits = request.data.get('credit')
        students = request.data.get('students')
        
        try:
            modules = Modules.objects.create(
                name=name,
                professor=professor,
                duration=duration,
                credits=credits,
                students=students
            )
            return Response({"message":"nouveau modules crée"},
                status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e :
            return Response({"message":str(e)})