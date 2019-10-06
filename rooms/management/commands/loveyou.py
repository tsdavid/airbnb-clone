from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This is command from loveyou.py "

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="how many times do you want me to tell you that i love you"
        )

    def handle(self, *args, **options):
        for t in range(0, int(options.get("times"))):
            self.stdout.write(self.style.ERROR("I love you"))
