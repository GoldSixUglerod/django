from api.models.User import User
from django.http import JsonResponse
from rest_framework import serializers, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password


from api.serializers.auth import LoginSerializer, RegistrationSerializer


class Auth(
    viewsets.GenericViewSet,
):
    """
    View list to authenticate and authorize
    """

    SERIALIZER_MAP = {  # we need different serializer depending on action
        "login": LoginSerializer,
        "register": RegistrationSerializer,
    }

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer: serializers.Serializer = self.SERIALIZER_MAP[self.action](
            data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.data["email"]).first()
        if user:
            return JsonResponse(
                {"error": "user with such email exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        registration_fields = {
            "email": serializer.validated_data.get("email"),
            "password": serializer.validated_data.get("password"),
            "first_name": serializer.validated_data.get("first_name"),
        }
        user = User.objects.create_user(**registration_fields)
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=False)
    def login(self, request):
        serializer: serializers.Serializer = self.SERIALIZER_MAP[self.action](
            data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        try:
            user: User = User.objects.get(email=serializer.validated_data.get("email"))
            if not check_password(serializer.data['password'], user.password):
                raise User.DoesNotExist
            # user: User = user.authenticate(
            #     email=serializer.validated_data.get("email"),
            #     password=serializer.validated_data.get("password"),
            # )  # Sends user to function to reduce number of requests to database
            if not user:
                raise User.DoesNotExist
        except User.DoesNotExist:  # If in any state user will be not found - login fails
            return JsonResponse(
                {"error": "user do not exist or invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({"token": token.key}, status=status.HTTP_200_OK)
