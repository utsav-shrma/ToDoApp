from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from djoser.serializers import UserSerializer as BaseCurrentUserSerializer

# serializer for creating user 
class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields=['id','username','email','password','first_name','last_name']


# serializer for listing and updating user details
class UserSerializer(BaseCurrentUserSerializer):
    class Meta(BaseCurrentUserSerializer.Meta):
        fields=['id','username','email','first_name','last_name']
