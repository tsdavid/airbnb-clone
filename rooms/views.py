from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)  # paginator 생성, orphans는 마지막 페이지에 기준 10하고 남은 나머지를 넣는 것
    try:
        rooms = paginator.page(int(page))  # page를 넣어서 paginator
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        # rooms = paginator.page(1)
        return redirect("/")
