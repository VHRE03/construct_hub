from rest_framework import viewsets
from .models import Worker
from .serializer import WorkerSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all().order_by('id')
    serializer_class = WorkerSerializer