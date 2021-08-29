from phonenumber_field.serializerfields import PhoneNumberField
from .DepartmentSerializer import DepartmentSerializer
from rest_framework import serializers

from ..models import Department


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="ID")
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    status = serializers.ChoiceField(
        [
            ("active", "User that working"),
            ("fired", "Fired user"),
            ("on_holiday", "User on holiday"),
        ]
    )
    age = serializers.IntegerField()
    main = serializers.BooleanField()
    department = DepartmentSerializer()
    telegram = serializers.CharField()
    phone_number = PhoneNumberField()
