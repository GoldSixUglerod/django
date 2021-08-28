from django.db import models
from django_postgres_extensions.models.fields import ArrayFields


class Action(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    vector_name = ArrayFields(models.FloatField)
    description = models.TextField(max_length=1000, null=True, default="")
