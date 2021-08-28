from django.db import models
from django.contrib.postgres.fields import ArrayField


class Action(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    keywords = ArrayField(models.CharField(max_length=50))
    keywords_vectorized = ArrayField(models.FloatField())
    description = models.TextField(max_length=1000, null=True, default="")

    def __str__(self):
        return str(self.name)
