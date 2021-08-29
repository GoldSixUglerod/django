from django.db import models
from django.utils.translation import gettext_lazy as _


class UserStatus(models.TextChoices):
    active = "active", "User that working"
    fired = "fired", "Fired user"
    on_holiday = "on_holiday", "User on holiday"
