from rest_framework import viewsets
from .models import TaskAssignment
from .serializer import TaskAssignmentSerializer

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all().order_by('task')
    serializer_class = TaskAssignment