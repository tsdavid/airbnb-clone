from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "price"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    # request get 한 부분이 blank일 때 ANywhere로 돌림.
    # if city is Anywhere dont filter by city
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    # if country is KR dont filter by country
    room_type = int(request.GET.get("room_type", 0))

    price = int(request.GET.get("price", 0))
    guest = int(request.GET.get("guest", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))

    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))

    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    # everything that i get from request, go to form
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guest": guest,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "superhost": superhost
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    # everything that i get from models, go to choices
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities

    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city
    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk__exact"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guest != 0:
        filter_args["guest__gte"] = guest

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True
    
    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)
    # print(s_amenities) => ["1", "2", "3"]

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)
            
    rooms = models.Room.objects.filter(**filter_args)
    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})
    # ** 하면 unpack 다 풀어놓는 개념인듯
