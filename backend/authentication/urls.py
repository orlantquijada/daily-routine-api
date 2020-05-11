from rest_framework_simplejwt import views as jwt_views

from django.urls import path, include

from backend.authentication import views


urlpatterns = path('obtain/', views.ObtainToken.as_view())
urlpatterns = [
    path('obtain/', views.ObtainToken.as_view()),
    path('refresh/', jwt_views.TokenRefreshView.as_view()),
    path('verify/', jwt_views.token_verify)
]
