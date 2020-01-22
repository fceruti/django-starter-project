# This is a temporary workaround till Poetry supports scripts, see
# https://github.com/sdispater/poetry/issues/241.
from subprocess import check_call


def server() -> None:
    check_call(["python", "manage.py", "runserver_plus"])


def tests() -> None:
    check_call(["pytest", "tests/"])


def worker() -> None:
    check_call(["python", "manage.py", "celery_autoreload"])


def migrate() -> None:
    check_call(["python", "manage.py", "migrate"])


def makemigrations() -> None:
    check_call(["python", "manage.py", "makemigrations"])


def shell() -> None:
    check_call(["python", "manage.py", "shell_plus"])
