from rest_framework import serializers
from backend.utils import global_vars


class TaskQuerySerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)


class RecordQuerySerializer(serializers.Serializer):
    week_no = serializers.IntegerField(required=False)
    auto_create = serializers.BooleanField(required=False)
    date = serializers.DateField(format=global_vars.DATE_FORMAT, input_formats=(
        global_vars.DATE_FORMAT,), required=False)

    def validate(self, attrs):
        week_no = attrs.get('week_no')
        auto_create = attrs.pop('auto_create')

        if week_no and not attrs:
            raise serializers.ValidationError(
                'Week Number query parameter must only be used as a solo query parameter.')

        attrs['auto_create'] = auto_create

        return attrs
