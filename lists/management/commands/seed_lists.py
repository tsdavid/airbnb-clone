import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"


class Command(BaseCommand):

    help = f"This is command that create {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"how many {NAME} do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        # seed를 통해서 모델에 row들을 만들어 주고
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users)}
        )
        created = seeder.execute()
        cleand = flatten(list(created.values()))
        for pk in cleand:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)
            # *를 안 붙이면, QUeryset이 array로 되어있는걸 그대로 저장함
            # *를 붙이면 array안에 있는 데이터를 저장해줌

        # seed를 통해 만들어진 row의 데이터들으
        # Query로 저장한다.

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
