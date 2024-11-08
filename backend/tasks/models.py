from django.db import models
from phases.models import Phase

class Task(models.Model):
    name = models.CharField(max_length=100, null=None)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name