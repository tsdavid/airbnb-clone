from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # it can show and hide
                "fields": ("amenities", "facilities", "house_rule"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

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
    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",  # User의 키를 필터링 할 수 잇다.
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )
    # list_filter는 해당 정보로 필터링 하는 것

    search_fields = ("=city", "^host__username")
    # admin에서 다른 foreign key를 하려면 __ 를 써야하나봄

    filter_horizontal = ("amenities", "facilities", "house_rule")
    # filter_horizontal only use when ManytoMany relationship


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
