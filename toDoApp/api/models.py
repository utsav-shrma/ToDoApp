from django.db import models
from toDoApp.settings import AUTH_USER_MODEL

# Create your models here.
class TaskList(models.Model):
    task=models.CharField(max_length=255)
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)