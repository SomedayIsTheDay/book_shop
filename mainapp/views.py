from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Genre
from django.conf import settings
import json

with open((settings.JSON_ROOT / "misc_data.json"), "r", encoding="utf-8") as f:
    data_json = json.load(f)


def index(request):

    return render(
        request,
        "mainapp/index.html",
        {
            "books": Book.objects.filter(is_active=True).order_by("?")[:3],
            "features": data_json["features"],
            "reviews": data_json["reviews"],
        },
    )


def books(request):
    return render(
        request,
        "mainapp/book_list.html",
        {
            "books": Book.objects.filter(is_active=True),
            "genres": Genre.objects.filter(is_active=True),
            "authors": Author.objects.filter(is_active=True),
            "title": "Books",
        },
    )


def book(request, pk):
    book_obj = get_object_or_404(Book, pk=pk)
    authors = book_obj.authors.all()
    return render(
        request,
        "mainapp/book.html",
        {"book": book_obj, "title": "Book", "authors": authors},
    )


def contacts(request):
    return render(request, "mainapp/contacts.html")
