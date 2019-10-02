from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    list_display = ("__str__", "rating_average")  # __str__ 하면 model에서 설정한 str을 불러온다.
    # way to use str in model at list_display
