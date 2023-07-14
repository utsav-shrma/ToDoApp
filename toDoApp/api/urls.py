from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

# handles routing based on viewset
router=SimpleRouter() 
router.register('todo',views.toDoViewSet)
urlpatterns = router.urls