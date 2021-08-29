from rest_framework import serializers

from api.models import User


class UserReadSerializer(serializers.ModelSerializer):
    """Serializer for getting user"""

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_activated",
            "is_staff",
        ]
        read_only_fields = fields
