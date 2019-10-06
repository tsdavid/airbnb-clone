import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

# seed_room에 user model을 가지고 온 이유는
# Room model에서 foreign 키로 user를 받기 때문에 seed 할떄
# foreign key 설정을 안하면 error 가 나옴


class Command(BaseCommand):

    help = "This is command that create Rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="how many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_room_type = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),  # seeder faker
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_room_type),
                "price": lambda x: random.randint(0, 300),
                "guests": lambda x: random.randint(1, 20),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
