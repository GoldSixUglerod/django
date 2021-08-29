from phonenumber_field.serializerfields import PhoneNumberField
from .DepartmentSerializer import DepartmentSerializer
from rest_framework import serializers

from ..models import Department, Employee, User


class EmployeeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    first_name = serializers.CharField(max_length=100, required=False)
    status = serializers.ChoiceField(
        [
            ("active", "User that working"),
            ("fired", "Fired user"),
            ("on_holiday", "User on holiday"),
        ], required=False
    )
    age = serializers.IntegerField(required=False)
    main = serializers.BooleanField(required=False, default=False)
    department_id = serializers.IntegerField(required=False)
    telegram = serializers.CharField(required=False)
    phone_number = PhoneNumberField(required=False)

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(**{"email": validated_data.get('email'),
                               "last_name": validated_data.get('last_name'),
                               "first_name": validated_data.get('first_name')})
        validated_data.pop('last_name')
        validated_data.pop('first_name')
        validated_data.pop('email')

        validated_data['department'] = Department.objects.get(id=validated_data.get("department_id"))
        validated_data['user_id'] = user.id

        return Employee.objects.create(**validated_data)
