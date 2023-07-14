
from rest_framework import serializers
from api.models import TaskList

# Serializer for admin user
class TaskListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskList
        fields=['id','task','user']

# Serializer for user 
class TaskListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskList
        fields=['id','task']
        


