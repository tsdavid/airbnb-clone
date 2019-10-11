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
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    # everything that i get from request, go to form
    form = {
        "city": city,
        "s_room_type": room_type, 
        "s_country": country
    }
    # everything that i get from models, go to choices
    choices = {
        "contries": countries, 
        "room_types": room_types
    }

    return render(request, "rooms/search.html", {**form, **choices})
    # ** 하면 unpack 다 풀어놓는 개념인듯
