from rest_framework import serializers
from Students.models import Students
from Professor.models import Professor

class StudentsSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        
class ProfessorSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'