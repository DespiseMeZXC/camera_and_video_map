import os
import sys


def start():
    os.system("python src/manage.py makemigrations")


def migrate():
    os.system("alembic upgrade head")


def makemigrations():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Необходимо указать сообщение для миграции")
        print("Использование: poetry run makemigrations 'your message'")
        sys.exit(1)

    message = sys.argv[1]
    os.system(f"alembic revision --autogenerate -m '{message}'")
