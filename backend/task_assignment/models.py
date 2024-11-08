from django.db import models
from tasks.models import Task
from workers.models import Worker

class TaskAssignment(models.Model):
    status_choices = [
        ('not_started', 'Sin iniciar'),
        ('in_progress', 'En progreso'),
        ('paused', 'Pausado'),
        ('completed', 'Completado')
    ]
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_choices, default='not_started')
    
    def __str__(self):
        return f"{self.task} - {self.worker} - {self.status}"
    