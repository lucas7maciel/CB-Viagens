from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from users.models import CustomUser

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = CustomUser
        fields = '__all__'#('username', 'first_name', 'last_name', 'email', 'password', 'phone_number')

    def to_representation(self, instance):
        data = super(UserRegistrationSerializer, self).to_representation(instance)
        user_tokens = RefreshToken.for_user(instance)
        tokens = {
            'refresh': str(user_tokens), 
            'access': str(user_tokens.access_token)
        }

        data = {
            "success": "true",
            "data": data | tokens
        }
        print(data)
        
        token, created = Token.objects.get_or_create(user=instance)
        print(token)
        print(created)

        return data