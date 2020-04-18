from rest_framework import mixins, viewsets

from backend.tasks import models, serializers


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    # pylint: disable=no-member
    queryset = models.Task.objects
    serializer_class = serializers.base.TaskSerializer

    def get_queryset(self):

        queryset = self.queryset

        serializer = serializers.query.TaskQuerySerializer(
            data=self.request.query_params
        )

        if not serializer.is_valid():
            return queryset.all()

        user_id = serializer.validated_data.get('user_id', None)
        if user_id:
            queryset = queryset.of_user(user_id)

        return queryset.all()
