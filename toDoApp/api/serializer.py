
from rest_framework import serializers
from api.models import TaskList

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskList
        fields=['id','task','user']

