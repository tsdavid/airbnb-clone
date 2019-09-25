from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Django Defualt User Admin이 따로 있음
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # fieldsets는 ADMIN Pannel에서 보여주는 부분인데
    # user 측 admin을 defualt된 걸 불러왔으니까, 새롭게 추가한 avatar, gender, currency등은 admin에 나타나지 않음
    # 그래서 fieldsets를 기존에 UserAdmin꺼에
    # 우리가 새롭게 추가한 필드를 넣어주는 거다
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),  # sub title
    )

