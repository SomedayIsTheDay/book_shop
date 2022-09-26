from django.core.management.base import BaseCommand
from mainapp.models import Genre, Book, Author
from authapp.models import BookUser
from django.conf import settings
from decouple import config
import json
import os


def load_from_json(filename):
    with open(
        os.path.join(settings.JSON_ROOT, filename + ".json"), "r", encoding="utf8"
    ) as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        genres = load_from_json("genres")

        Genre.objects.all().delete()
        for genre in genres:
            Genre.objects.create(name=genre)

        authors = load_from_json("authors")

        Author.objects.all().delete()
        for author in authors:
            Author.objects.create(**author)

        books = load_from_json("books")

        Book.objects.all().delete()
        for book in books:
            book["genre"] = Genre.objects.get(name=book["genre"])
            authors = []
            for author in book["authors"]:
                first_name, last_name = author.split()
                author_obj = Author.objects.get(
                    first_name=first_name, last_name=last_name
                )
                authors.append(author_obj)
            del book["authors"]
            book = Book.objects.create(**book)
            book.authors.set(authors)

        if not BookUser.objects.filter(username="admin"):
            BookUser.objects.create_superuser(
                username="admin",
                email="admin@localhost",
                password=config("ADMIN_PASSWORD"),
                age=100,
            )
