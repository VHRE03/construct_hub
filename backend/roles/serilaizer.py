from rest_framework import serializers
from .models import Role
from rest_framework import exceptions

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        