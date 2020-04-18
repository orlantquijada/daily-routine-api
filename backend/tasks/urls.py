from django.urls import path, include

from rest_framework import routers

from backend.tasks import views


ROUTER = routers.DefaultRouter()
ROUTER.register('tasks', views.TaskViewSet)

urlpatterns = path('', include(ROUTER.urls))
