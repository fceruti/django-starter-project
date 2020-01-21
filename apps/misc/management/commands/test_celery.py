from django.core.management.base import BaseCommand

from apps.misc.tasks import task_dummy


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        task_dummy.delay(1, 2)
