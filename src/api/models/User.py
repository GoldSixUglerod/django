from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.indexes import HashIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    email = models.EmailField(_("Email address"), unique=True)

    first_name = models.CharField(
        max_length=100,
        verbose_name=_("user name"),
        null=True,
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_("user surname"),
        null=True,
        blank=True,
    )

    is_activated = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        indexes = [
            HashIndex(fields=["email"]),
        ]
