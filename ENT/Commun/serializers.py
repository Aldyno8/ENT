from rest_framework import serializers
from Commun.models import *

# serializers des modules
class ModulesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = ('id', 'Name', 'Duration', 'Credit')
        
# sérializers des contenu de modules
class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

# serialiers des events
class EventSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'Name', 'Description', 'start', 'end')