from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

from api.models import Employee
from django.db.models import PROTECT


class Task(models.Model):
    name = models.CharField(max_length=50, blank=True, default="")
    description = models.TextField(max_length=1000, null=False, blank=False)
    list_targets = ArrayField(models.CharField(max_length=50), default=list)
    end_time_best = models.DateField(null=False)
    expected_period_days = models.IntegerField(null=False)
    end_time_actual = models.DateField(null=True)
    finished = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(100)], null=True)
    employee = models.ForeignKey(Employee, null=True, on_delete=PROTECT)
