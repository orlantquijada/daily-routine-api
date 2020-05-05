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
        fields = ('id', 'user_id', 'title', 'start_time', 'duration', 'icon')

    def validate(self, attrs):
        start_time = attrs.get('start_time', None)
        duration = attrs.get('duration', None)

        attrs['title'] = attrs['title'].capitalize()

        if not start_time and not duration:
            return attrs

        if start_time and not duration:
            raise serializers.ValidationError(
                'Start time must have a duration.')

        return attrs


class RecordSerializer(serializers.ModelSerializer):

    task_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Task.objects.all(),
        source='of_task'
    )
    date = serializers.DateField(
        format=global_vars.DATE_FORMAT, input_formats=(global_vars.DATE_FORMAT))

    class Meta:
        model = models.Record
        fields = ('id', 'task_id', 'date', 'is_accomplished')

    def create(self, validated_data):
        # pylint: disable=unused-variable
        obj, created = models.Record.objects.get_or_create(**validated_data)

        return obj
