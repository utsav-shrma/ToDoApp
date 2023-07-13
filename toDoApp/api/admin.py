from django.contrib import admin

# Register your models here.
from api.models import TaskList

admin.site.register(TaskList)