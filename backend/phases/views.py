from rest_framework import viewsets
from .models import Phase
from .serializer import PhaseSerializer

class PhaseViewSet(viewsets.ModelViewSet):
    queryset = Phase.objects.all().order_by('id')
    serializer_class = PhaseSerializer