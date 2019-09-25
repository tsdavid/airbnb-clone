from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = (
            True
        )  # DB로 가지 않는 모델, 다른 모델에서 확장해서 사용할 떄 주로 사용, users 모델에서 AbstractUser할 때도 abstract 사용함
