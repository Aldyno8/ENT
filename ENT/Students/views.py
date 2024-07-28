from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
# Class qui gère l'affichage des cours de l'étudiants
class ModulesList(APIView):
    def get(self, request):
        user = request.user # récupère les informations de l'user qui fait la requete
        try:
            students = Students.objects.get(id=user.id)
            course = students.modules.all()
            
            # Sérializers les donnés du cours
            course_serialize = ModulesSerializers(course, many=True)
            
            return Response (course_serialize.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# Class qui gère l'affichage des contenus de chaque cours
class ModulesContent(APIView):
    def get(self, request, id):
        try:
            content = Documents.objects.filter(id=id)
            if not content.exists():
                return Response({"message":"Ce module ne contient aucun cours pour l'instant"}, status=status.HTTP_204_NO_CONTENT)
            
            content_serializes = ContentSerializers(content, many=True)
            return Response(content_serializes.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)