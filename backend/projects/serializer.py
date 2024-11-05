from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        if end_date and start_date and end_date < start_date:
            raise serializers.ValidationError({
                'date_error': "La fecha de finalización no puede ser anterior a la fecha de inicio."
            })
        
        return data
