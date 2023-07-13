from api import serializer
from api.models import TaskList
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class toDoViewSet(ModelViewSet):
    queryset=TaskList.objects.all()
    serializer_class= serializer.TaskListAdminSerializer
    permission_classes=[IsAuthenticated]

    def get_serializer_class(self):
        if(self.request.user.is_staff):
            serializer_class= serializer.TaskListAdminSerializer
        else:
            serializer_class= serializer.TaskListUserSerializer
        return serializer_class

    def get_queryset(self):
        if(self.request.user.is_staff):
            queryset= TaskList.objects.all()
        else:
            queryset= TaskList.objects.filter(user=self.request.user)
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}


    
