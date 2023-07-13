from api import serializer
from api.models import TaskList
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class toDoViewSet(ModelViewSet):
    queryset=TaskList.objects.all()
    serializer_class= serializer.TaskListSerializer
    permission_classes=[IsAuthenticated]
    def get_serializer_context(self):
        return {'request': self.request}
