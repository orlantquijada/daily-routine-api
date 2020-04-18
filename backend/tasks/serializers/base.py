from rest_framework import serializers

from backend.utils import global_vars

from backend.tasks import models
from backend.users import models as users_models


class TaskSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=users_models.User.objects.all(),
        source='of_user'
    )

    start_time = serializers.TimeField(
        format=global_vars.TIME_FORMAT, input_formats=(global_vars.TIME_FORMAT,), required=False)
    duration = serializers.TimeField(
        format=global_vars.TIME_FORMAT, input_formats=(global_vars.TIME_FORMAT,), required=False)

    class Meta:
        model = models.Task
        fields = ('id', 'user_id', 'title', 'start_time', 'duration')

    def validate(self, attrs):
        start_time = attrs.get('start_time', None)
        duration = attrs.get('duration', None)

        if not start_time and not duration:
            return attrs

        if start_time and not duration:
            raise serializers.ValidationError(
                'Start time must have a duration.')

        return attrs
