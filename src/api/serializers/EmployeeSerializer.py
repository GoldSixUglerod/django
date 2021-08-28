from rest_framework import serializers

from ..models import Employee, Department


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID')
    email = serializers.EmailField()
    username = serializers.CharField()
    status = serializers.CharField()
    age = serializers.IntegerField()
    main = serializers.BooleanField()
    department = serializers.RelatedField(source='department', many=True, queryset=Department.objects.all())
    telegram = serializers.CharField()
    phone_number = serializers.CharField()
