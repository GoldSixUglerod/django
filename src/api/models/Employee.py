from django.db import models
from django.db.models import PROTECT
from phonenumber_field.modelfields import PhoneNumberField

from api.models.enums import UserStatus


class Employee(models.Model):
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        null=False,
        related_name="user",
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

    department = models.ForeignKey("Department", on_delete=PROTECT)

    telegram = models.CharField(max_length=256, null=True, blank=True)
    phone_number = PhoneNumberField(
        unique=True, verbose_name="Phone number. Contains region, and number itself", null=True
    )

    def to_json(self):
        return {
            "last_name": self.user.last_name,
            "first_name": self.user.first_name,
            "email": self.user.email,
            "status": self.status,
            "age": self.age,
            "main": self.main,
            "department": self.department.id,
            "telegram": self.telegram,
            "phone_number": self.phone_number
        }

    class Meta:
        app_label = "api"
