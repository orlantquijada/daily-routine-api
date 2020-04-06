from rest_framework import mixins, viewsets, permissions
from rest_framework.decorators import permission_classes

from backend.users import models, serializers


class UserViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.base.UserSerializer

    def get_permissions(self):

        if self.action == 'create':
            return [permissions.AllowAny()]

        return super().get_permissions()
