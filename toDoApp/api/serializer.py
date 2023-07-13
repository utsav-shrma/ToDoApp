
from rest_framework import serializers
from api.models import TaskList
from user.serializer import UserSerializer

class TaskListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskList
        fields=['id','task','user']
    

class TaskListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskList
        fields=['id','task']
        


