from django.db import models
from django.utils.translation import ugettext as _

from apps.common.models import TimeStampUUID
from apps.profiles.models import Profile
from project.settings.base import AUTH_USER_MODEL


class Rating(TimeStampUUID):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name="USer providing the rating",
        on_delete=models.SET_NULL,
        null=True,
    )
    agent = models.ForeignKey(
        Profile,
        verbose_name=_("Agent"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="agent_review",
    )

    rating = models.IntegerField(
        verbose_name=_("Rating"),
        default=0,
        choices=Range.choices,
        help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
    )

    comment = models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ["agent", "rater"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
