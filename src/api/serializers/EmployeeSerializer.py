from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from ..models import enums, Department


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID')
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    status = serializers.ChoiceField(enums)
    age = serializers.IntegerField()
    main = serializers.BooleanField()
    department = serializers.RelatedField(source='department', many=True, queryset=Department.objects.all())
    telegram = serializers.CharField()
    phone_number = PhoneNumberField()
