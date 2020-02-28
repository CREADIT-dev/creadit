from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'display_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        email: str = validated_data['email']
        display_name: str = validated_data['display_name']
        password: str = validated_data['password']

        User.objects.create_user(email=email, display_name=display_name, password=password)
        return validated_data


class SignInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, validated_data) -> User:
        user = authenticate(**validated_data)

        if user is not None and user.is_active:
            return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('display_name', 'email')
