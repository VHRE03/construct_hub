from django.db import models
from django.core.exceptions import ValidationError

class Project(models.Model):
    name = models.CharField(max_length=100, null=None)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
     