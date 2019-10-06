from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):
    # Inline  종류가 있다 admin에서 보여지는 방식에 차이가 있을 뿐
    # TabularInline, StackedInline  취향 따라 가자

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
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
        "count_amenities",  # 함수를 스트링 형식으로
        "count_photos",
        "total_rating",
    )
    # list_display는 어드민 패널에서 정보를 보여주는 역할

    ordering = ("name", "price", "bedrooms")

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

    raw_id_fields = ("host",)
    # raw_id_fiedls는 Foriegn key를 id로 나타내서 관리하기 용기하기 만듬

    search_fields = ("=city", "^host__username")
    # admin에서 다른 foreign key를 하려면 __ 를 써야하나봄

    filter_horizontal = ("amenities", "facilities", "house_rule")
    # filter_horizontal only use when ManytoMany relationship

    def count_amenities(self, obj):  # self는 class에서 받은거, obj는 row에 해당한다.
        # print(obj.amenities.all())  # return : The David's House 라고 나옴, row를 호출하네
        # obj는 row에 해당하고 print된거는 __str__ 때문에 house name이 나오는거 임
        # 해당 obj에 요소로 들어갈 수 있음
        # 정말 멋지다.
        # obj.amenities.all() -> <QuerySet [<Amenity: WiFi>]>: QuerySet이 나옴
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Counts"

    # count_amenities.short_description = "Hello Sexy"  # 와우 이렇게 하면 위 타이틀을 변경할 수 있음


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumnail")

    def get_thumnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')
        # mark_safe는 기본적으로 장고가 정보보호를 위해서 html태그를 발동 못하게 막아놓을 걸
        # 태그를 활성화 할 수 있게 하는 거임

    get_thumnail.short_description = "Thumbnail"
