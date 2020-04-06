from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from backend.authentication import serializers


class ObtainToken(TokenObtainPairView):
    serializer_class = serializers.base.ObtainTokenSerializer
    permission_classes = (permissions.AllowAny,)
