from django.contrib import admin
from api.models import TaskList

#registering task list for admin panel
@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display=('task','user')