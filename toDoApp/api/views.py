from api import serializer
from api.models import TaskList
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class toDoViewSet(ModelViewSet):
    queryset=TaskList.objects.all()
    serializer_class= serializer.TaskListSerializer
    def get_serializer_context(self):
        return {'request': self.request}
