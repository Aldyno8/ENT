from rest_framework import serializers
from .models import *

# serializers des cours
class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'Name', 'Duration', 'Credit')