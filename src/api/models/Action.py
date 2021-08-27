from django.contrib.postgres.fields import ArrayField
from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    vector_name = models.FloatField()
    description = models.TextField(max_length=1000, null=True, default="")
