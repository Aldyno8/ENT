from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import *
from Students.models import Students
from Professor.models import Professor as Prof

# Create your views here.
class UserResigter(APIView):
    # {"username":"aldynot", "email":"aldynobruel@gmail.com", "password":"fake"}
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')
        try:
            created, user = User.objects.get_or_create(
                username=username,
                email=email, 
                password=password
            )
            if created:
                try:
                    if role == 'Etudiant':
                        students = Students.objects.create(
                            User = user,
                            Pseudo = request.data.get('pseudo'),
                            Niveau = request.data.get('niveau'),
                            Parcours = request.data.get('parcours'),
                            Age = request.data.get('age'),
                            birth = request.data.get('brith')
                            )
                        print(students)
                except Exception as e:
                    return Response({"message":"erreur de création de l'étudiant"},
                                    status=status.HTTP_400_BAD_REQUEST)
                
                else :
                    try:
                        Profeseur = Prof.objects.create(
                            User = user,
                            Speciality = request.data.get('speciality'),
                            )
                        print(Prof)
                    except Exception as e:
                        return Response({"message":"erreur de création de l'étudiant"},
                                        status=status.HTTP_400_BAD_REQUEST)
                        
                    
                return Response({"message":"User create successfully!"},
                status=status.HTTP_201_CREATED )
                
            else:
                return Response({"message":"un compte avec les meme identifiants exist déja"},
                                status=status.HTTP_400_BAD_REQUEST)
                
            
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        