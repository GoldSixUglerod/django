from rest_framework import serializers

from ..models import Department


class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    list_targets = serializers.ListField(
        child=serializers.CharField(), required=False, default=list
    )
    description = serializers.CharField(required=False, default="")

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.keywords = validated_data.get("keywords", instance.keywords)
        instance.description = validated_data.get("description", instance.description)

        instance.save()
        return instance


class DepartmentReadSerializer(serializers.ModelSerializer):
    """Serializer for getting department"""

    class Meta:
        model = Department
        fields = [
            "pk",
            "name",
            "list_targets",
            "description",
        ]
        read_only_fields = fields
