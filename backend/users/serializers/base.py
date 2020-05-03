from rest_framework import serializers

from backend.utils import global_vars

from backend.users import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'profile_pic', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        obj = models.User.objects.create_user(**validated_data)

        return obj

    def update(self, instance, validated_data):
        pw = validated_data.get('password')
        if pw:
            raise serializers.ValidationError(
                'Password can not be updated through this request url. Use "/api/v1/users/change-password/ instead.')

        return validated_data

    def validate(self, attrs):
        first_name = attrs.get('first_name', None)
        last_name = attrs.get('last_name', None)

        if first_name:
            attrs['first_name'] = self._clean_name(first_name)
        if last_name:
            attrs['last_name'] = self._clean_name(last_name)

        return attrs

    def _clean_name(self, name):
        if name is not None:
            return name.title()
        return


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if new_password != confirm_password:
            raise serializers.ValidationError('Passwords do not match!')

        if new_password == old_password:
            raise serializers.ValidationError(
                'Old Password and New Password must not match!')

        return attrs
