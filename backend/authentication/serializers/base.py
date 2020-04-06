from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ObtainTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(ObtainTokenSerializer, cls).get_token(user)

        token['full_name'] = user.full_name()
        return token
