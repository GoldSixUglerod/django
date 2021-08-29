from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(
        self, email: str, password: str = None, commit=True, **extra_fields
    ):
        """
        Create and save a user with the given email adn password.
        """
        user = self.model(email=email, password=password, **extra_fields)
        if password is not None:
            user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **extra_fields):
        """This function creates regular user."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        """This function helps to create superuser with needed privileges"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_activated", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password=password, **extra_fields)
