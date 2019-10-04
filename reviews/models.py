from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        # return self.room.host.username  # 다른 모델들의 키를 가지고 올수 있다.,
        # 모델의 모델을 찾아서 Foreign key로 모델 깊이로 들어감
        return f"{self.review} - {self.room}"  # 이렇게 작성하니까 너무 편하네

    # Room에서 amedities 숫자 새고 하는 건 admin 쪽에서만 필요하니까, admin.py에서 진행했는데
    # reviews같은 곳은 admin 뿐만 아니라 public에서도 사용해야하니까
    # model.py에서 숫자, 평균을 내는 함수를 만든다.
    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "AVG."
