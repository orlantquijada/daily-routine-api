from django.urls import path, include

from backend.authentication import views

urlpatterns = path('obtain/', views.ObtainToken.as_view())
