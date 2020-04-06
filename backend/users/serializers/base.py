from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from backend.utils import global_vars

from backend.users import models


class UserSerializer(serializers.ModelSerializer):
    profile_pic = Base64ImageField(required=False)

    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'profile_pic', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        obj = models.User.objects.create_user(**validated_data)

        return obj

    def validate(self, validated_data):
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)

        validated_data['first_name'] = self.clean_name(first_name)
        validated_data['last_name'] = self.clean_name(last_name)

        return validated_data

    def clean_name(self, name):
        if name is not None:
            return name.title()
        return name
