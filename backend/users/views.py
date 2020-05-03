from rest_framework import mixins, viewsets, permissions
from rest_framework.decorators import permission_classes, action
from rest_framework.response import Response

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

    @action(detail=True, methods=['post'], url_path='change-password')
    def change_password(self, request, pk):
        serializer = serializers.base.ChangePasswordSerializer(
            data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        try:
            user = models.User.objects.get(id=pk)
        except:
            return Response({'error': 'User does not exist.'})

        old_password = serializer.validated_data.get('old_password')
        if not user.check_password(old_password):
            return Response({'error': 'Old password does not match with User.'})

        new_password = serializer.validated_data.get('new_password')
        user.set_password(new_password)
        user.save()

        return Response(self.serializer_class(user).data)
