from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):
    help = "This is command that create Amenities "

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="how many times do you want me to tell you that i love you"
    #     )

    def handle(self, *args, **options):
        rules = [
            "No Smoking",
            "No Pet",
            "No Company",
            "No Party",
            "No Drinks",
            "No Cook",
            "No BBQ",
            "NO NO NO"

        ]
        for rule in rules:
            HouseRule.objects.create(name=rule)
            # Amenity model에 Name이 있으니까 그걸로 저장하는 걸 지정해주는 듯
        self.stdout.write(self.style.SUCCESS("House Rules created!"))
