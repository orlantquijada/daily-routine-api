from rest_framework import serializers

from backend.tasks.serializers import base


class ExtendedRecordSerializer(base.RecordSerializer):
    task = base.TaskSerializer(read_only=True, source='of_task')

    class Meta:
        model = base.RecordSerializer.Meta.model
        fields = base.RecordSerializer.Meta.fields + ('task',)
