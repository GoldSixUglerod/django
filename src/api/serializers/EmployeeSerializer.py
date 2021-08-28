from rest_framework import serializers

from ..models import Employee, Action


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID')
    email = serializers.EmailField()
    username = serializers.CharField()
    status = serializers.CharField()
    age = serializers.IntegerField()
    main = serializers.BooleanField()
    action = serializers.RelatedField(source='action', many=True)
    telegram = serializers.CharField()
    phone_number = serializers.CharField()
