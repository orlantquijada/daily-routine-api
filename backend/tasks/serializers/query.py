from rest_framework import serializers


class TaskQuerySerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
