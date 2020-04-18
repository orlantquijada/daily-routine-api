from rest_framework_simplejwt import views as jwt_views

from django.contrib import admin
from django.urls import path, include

from backend.users.urls import urlpatterns as USER_URLS
from backend.tasks.urls import urlpatterns as TASK_URLS
from backend.authentication.urls import urlpatterns as AUTH_URLS


JWT_URLS = path('token/', include([
    AUTH_URLS,
    path('refresh/',
         jwt_views.TokenRefreshView.as_view())
]))

urlpatterns = (
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        USER_URLS,
        TASK_URLS,
        JWT_URLS
    ]))
)
