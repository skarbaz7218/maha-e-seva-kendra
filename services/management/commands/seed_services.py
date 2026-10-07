from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Service management is handled through Django Admin"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(
                "Services are managed through Django Admin Panel."
            )
        )