from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This is command that create Facilities "

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="how many times do you want me
    # to tell you that i love you"
    #     )

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
            # Amenity model에 Name이 있으니까 그걸로 저장하는 걸 지정해주는 듯
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
