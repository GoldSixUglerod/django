from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from api.models import Action
from api.models.enums import UserStatus


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        primary_key=True,
    )
    status = models.CharField(
        max_length=100,
        choices=UserStatus.choices,
        default=UserStatus.active,
        help_text="User role",
    )

    age = models.PositiveIntegerField(null=True, blank=True)
    main = models.BooleanField(default=False)

    action = models.ForeignKey(Action, on_delete=models.PROTECT, related_name="employee")

    telegram = models.CharField(max_length=256, null=True, blank=True)
    phone_number = PhoneNumberField(
        unique=True, verbose_name="Phone number. Contains region, and number itself"
    )
