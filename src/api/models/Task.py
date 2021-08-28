from django.db import models
from django.contrib.postgres.fields import ArrayField


class Task(models.Model):
    description = models.TextField(max_length=1000, null=False, blank=False)
    list_targets = ArrayField(models.CharField(max_length=50), default=list)
