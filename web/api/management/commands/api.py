from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "api command"

    def handle(self, *args, **options):
        print("Hello World!")