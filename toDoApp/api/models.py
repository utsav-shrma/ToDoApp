from django.db import models
from toDoApp.settings import AUTH_USER_MODEL

# Model for todo list items
class TaskList(models.Model):
    task=models.CharField(max_length=255)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)