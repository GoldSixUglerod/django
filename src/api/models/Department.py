from django.db import models
from django.contrib.postgres.fields import ArrayField


class Department(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    list_targets = ArrayField(models.CharField(max_length=50), default=list)
    description = models.TextField(max_length=1000, null=True, default="")

    def __str__(self):
        return str(self.name)
git