from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampUUID

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampUUID):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+923024242421"
    )
    about_me = (
        models.TextField(
            verbose_name=_("About Me"), default="Say something about yourself"
        ),
    )
    lisence = models.CharField(
        verbose_name=_("Real Estate Lisence"), max_length=255, null=True, blank=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png", max_length=255
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"),
        default="Pakistan",
        null=False,
        blank=False,
        max_length=255,
    )
    city = models.CharField(
        verbose_name=_("City"),
        default="Lahore",
        max_length=180,
        null=False,
        blank=False,
    )
    is_buyer = models.BooleanField(
        verbose_name="Buyer",
        default=False,
        help_text="Are you a looking to buy a property?",
    )
    is_seller = models.BooleanField(
        verbose_name="Seller",
        default=False,
        help_text="Are you a looking to sell a property?",
    )
    is_agent = models.BooleanField(
        verbose_name="Agent",
        default=False,
        help_text="Are you an agent?",
    )
    top_agent = models.BooleanField(verbose_name="Top Agent", default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_of_reviews = models.IntegerField(
        verbose_name="Number of reviews", default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}"
