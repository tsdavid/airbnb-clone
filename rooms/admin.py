from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
    # list_display는 어드민 패널에서 정보를 보여주는 역할
    list_filter = ("instant_book", "city", "country")
    # list_filter는 해당 정보로 필터링 하는 것

    search_fields = ("=city", "^host__username")
    # admin에서 다른 foreign key를 하려면 __ 를 써야하나봄


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
