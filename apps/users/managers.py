from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except (ValidationError):
            raise ValidationError(_("Invalid email address"))

    def create_user(self, username, first_name, last_name, email, password, **kwargs):
        if not username:
            raise ValidationError(_("Username must not be empty"))
        if not first_name:
            raise ValidationError(_("Firstname must not be empty"))
        if not last_name:
            raise ValidationError(_("Lastname must not be empty"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValidationError(_("Email must not be empty"))

        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **kwargs
        )

        user.set_password(password)
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)

        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, password, **kwargs
    ):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_superuser") is not True:
            raise ValidationError(_("Superuser must havae is_superuser=True"))
        if kwargs.get("is_staff") is not True:
            raise ValidationError(_("Superuser must havae is_staff=True"))
        if not password:
            raise ValidationError(_("Password must not be empty"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValidationError(_("Email must not be empty"))

        user = self.create_user(
            username, first_name, last_name, email, password, **kwargs
        )

        user.save(using=self._db)

        return user
