from rest_framework import serializers

from ..models import Department


class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    list_targets = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    description = serializers.CharField(required=False, default="")

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.list_targets = validated_data.get("list_targets", instance.list_targets)
        instance.description = validated_data.get("description", instance.description)

        instance.save()
        return instance
