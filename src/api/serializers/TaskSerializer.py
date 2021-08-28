from rest_framework import serializers

from ..models import Task


class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_blank=False)
    description = serializers.CharField(max_length=1000, allow_blank=False)
    list_targets = serializers.ListField(child=serializers.CharField(max_length=50))
    end_time_best = serializers.DateField()
    end_time_actual = serializers.DateField()
    finished = serializers.BooleanField(default=False)
    score = serializers.IntegerField(default=5, min_value=1, max_value=10)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.end_time_actual = validated_data.get("end_time_actual", instance.end_time_actual)
        instance.description = validated_data.get("description", instance.description)
        instance.finished = validated_data.get("finished", instance.finished)
        instance.score = validated_data.get("score", instance.score)

        instance.save()
        return instance
