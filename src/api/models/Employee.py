from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
import Action


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        null=False,
        primary_key=True,
    )
    status = models.CharField(null=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    main = models.BooleanField(default=False)

    action = models.CharField(null=True)

    telegram = models.CharField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True)
