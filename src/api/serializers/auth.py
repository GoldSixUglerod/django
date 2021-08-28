from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("User with this email exists")
        return email

    class Meta:
        model = User
        fields = ("email", "password", "first_name")
        extra_kwargs = {"password": {"required": True, "write_only": True}}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_null=False)
    password = serializers.CharField(required=True, allow_null=False)
