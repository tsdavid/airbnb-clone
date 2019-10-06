import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
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
        # seeder.excute()를 통해서 room을 만들고
        # 만든 room의 pk 번호를 기준으로
        # 사진을 url형식으로 pk를 통해 저장한다.
        created_photo = seeder.execute()
        created_clean = flatten(list(created_photo.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)  # 왜 이걸 2로 나누는 것만 가능한지 이해가 안함
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)  # 왜 이걸 2로 나누는 것만 가능한지 이해가 안함
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rule.add(r)  # 왜 이걸 2로 나누는 것만 가능한지 이해가 안함
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
