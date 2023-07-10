from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path,include

router=SimpleRouter() 
router.register('todo',views.toDoViewSet)
urlpatterns = router.urls