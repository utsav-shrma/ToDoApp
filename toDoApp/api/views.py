from api import serializer
from api.models import TaskList
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Viewset for handling todo task list
class toDoViewSet(ModelViewSet):

    queryset=TaskList.objects.all()
    serializer_class= serializer.TaskListAdminSerializer

    #overriding create funstion to append user id for normal user
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)    
        serializer.is_valid(raise_exception=True)
        if (not self.request.user.is_staff):
            serializer.validated_data['user'] = self.request.user
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        def get_success_headers(self, data):
            try:
                return {'Location': str(data[api_settings.URL_FIELD_NAME])}
            except (TypeError, KeyError):
                return {}

    # Limiting endpoint access to only logged in users
    permission_classes=[IsAuthenticated]

    # Overiding serializer depending upon user
    def get_serializer_class(self):
        if(self.request.user.is_staff):
            serializer_class= serializer.TaskListAdminSerializer
        else:
            serializer_class= serializer.TaskListUserSerializer
        return serializer_class

    # Overiding queryset depending upon user
    def get_queryset(self):
        if(self.request.user.is_staff):
            queryset= TaskList.objects.all()
        else:
            queryset= TaskList.objects.filter(user=self.request.user)
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}


    
