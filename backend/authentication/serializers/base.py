from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from backend.users import serializers


class ObtainTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(ObtainTokenSerializer, cls).get_token(user)

        token['full_name'] = user.full_name()
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = serializers.base.UserSerializer(self.user).data
        return data
