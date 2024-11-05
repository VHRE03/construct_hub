from django.db import models
from projects.models import Project

class Phase(models.Model):
    name = models.CharField(max_length=100, null=None)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    