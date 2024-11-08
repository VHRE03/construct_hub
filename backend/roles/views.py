from rest_framework import viewsets
from .models import Role
from .serilaizer import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('id')
    serializer_class = RoleSerializer