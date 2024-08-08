from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Commun.serializers import ModulesSerializers, ContentSerializers
from .models import *
from Commun.models import Modules, Documents
#  from .seriarilzers import *

# Create your views here.
class ModuleListView(APIView):
    def get(self, request):
        user = request.user
        print(user)
        
        try:
            prof = user.prof
            modules = prof.modules.all()
            modules_serializes = ModulesSerializers(modules, many=True)
            return Response(modules_serializes.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
                   
# class qui affiche la liste des contenus du Modules et permemt au prof de publier des contenus de cours
class ModulesContent(APIView):
    def get(self, request, id):
        try:
            modules = Modules.objects.get(id=id)
            content = modules.contents.all()
            
            if not content.exists():
               return Response({"message":"Ce module ne contient aucun cours pour l'instant"}, status=status.HTTP_204_NO_CONTENT)
            
            content_serializes = ContentSerializers(content, many=True)
            return Response(content_serializes.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, *args, **kwargs):
        modules_id = self.kwargs.get('id')
        modules = Modules.objects.get(id=modules_id)
        print(modules)
        name = request.data.get('name')
        file = request.data.get('file')
        
        if not name or not file:
            return Response({"message": "le nom et le fichier sont requis"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            Documents.objects.create(Modules=modules, Name=name, Link=file)
            return Response({"message":"Documents ajouter"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
