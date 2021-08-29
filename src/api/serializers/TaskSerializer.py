from rest_framework import serializers

from ..models import Employee, Task


class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_blank=True, default="")
    description = serializers.CharField(
        max_length=1000, allow_null=False, allow_blank=False
    )
    list_targets = serializers.ListField(
        child=serializers.CharField(max_length=50), default=list
    )
    end_time_best = serializers.DateField(allow_null=False)
    expected_period_days = serializers.IntegerField(allow_null=False)
    end_time_actual = serializers.DateField(allow_null=True)
    finished = serializers.BooleanField(default=False)
    score = serializers.IntegerField(
        default=5, min_value=1, max_value=10, allow_null=True
    )
    employee_id = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)

        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.list_targets = validated_data.get(
            "list_targets", instance.list_targets
        )
        instance.end_time_best = validated_data.get(
            "end_time_best", instance.end_time_best
        )
        instance.expected_period_days = validated_data.get(
            "expected_period_days", instance.expected_period_days
        )
        instance.end_time_actual = validated_data.get(
            "end_time_actual", instance.end_time_actual
        )
        instance.finished = validated_data.get("finished", instance.finished)
        instance.score = validated_data.get("score", instance.score)
        instance.employee_id = validated_data.get("employee_id", instance.employee_id)

        instance.save()
        return instance
