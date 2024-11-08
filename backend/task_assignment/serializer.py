from rest_framework import serializers
from .models import TaskAssignment

class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = '__all__'
        
    # Funcion para verificar la integridad de los datos