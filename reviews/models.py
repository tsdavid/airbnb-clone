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
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        # return self.room.host.username  # 다른 모델들의 키를 가지고 올수 있다., 모델의 모델을 찾아서 Foreign key로 모델 깊이로 들어감
        return f'{self.review} - {self.room}'   # 이렇게 작성하니까 너무 편하네
    