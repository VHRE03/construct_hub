from django.db import models
from roles.models import Role

class Worker(models.Model):
    name = models.CharField(max_length=100, null=None)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)