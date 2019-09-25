from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gende = models.CharField(
        default=GENDER_MALE,
        choices=GENDER_CHOICES,
        max_length=10,
        null=True,
        blank=True,
    )
    bio = models.TextField(default="", blank=True)  # blank 는 이 부분이 없어도 저장이 가능하게 넘겨주는거
