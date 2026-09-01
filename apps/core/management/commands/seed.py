from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Automates running makemigrations and migrate sequentially"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("1. Running makemigrations..."))
        call_command("makemigrations")

        self.stdout.write(self.style.WARNING("2. Running migrate..."))
        call_command("migrate")

        self.stdout.write(self.style.SUCCESS("Database schema updated successfully!"))