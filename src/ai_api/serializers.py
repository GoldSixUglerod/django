from rest_framework import serializers

from api.models.Action import Action
from api.models.Employee import Employee
from api.models.Leader import Leader
from api.models.Task import Task
from django.db.models import fields


class ActionSerializer(serializers.Serializer):
    name = serializers.CharField()
    keywords = serializers.ListField(child=serializers.CharField())
    keywords_vectorized = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))
    description = serializers.CharField()

    def create(self, validated_data):
        return Action.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.keywords = validated_data.get("keywords", instance.keywords)
        instance.keywords_vectorized = validated_data.get("keywords_vectorized", instance.keywords_vectorized)
        instance.description = validated_data.get("description", instance.description)

        instance.save()
        return instance
