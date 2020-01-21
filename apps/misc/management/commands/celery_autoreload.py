import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery(*args, **kwargs):
    print("Restarting celery...")
    autoreload.raise_last_exception()
    kill_worker_cmd = "ps aux | grep bin/celery | awk '{print $2}' | xargs kill -9"
    subprocess.call(kill_worker_cmd, shell=True)
    start_worker_cmd = "celery -A conf worker -l info"
    subprocess.call(shlex.split(start_worker_cmd))


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery, args=None, kwargs=None)
