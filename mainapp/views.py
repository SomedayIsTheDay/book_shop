from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import cache_page
from .models import Book, Author, Genre
from django.conf import settings
import json
import django_filters


class BookFilter(django_filters.FilterSet):
    genre = django_filters.NumberFilter(field_name="genre", lookup_expr="exact")

    class Meta:
        model = Book
        fields = ["genre"]


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


def books(request, page=1):
    book_list = Book.objects.filter(is_active=True)
    book_filtered = BookFilter(request.GET, book_list).qs
    paginator = Paginator(book_filtered, per_page=4)
    return render(
        request,
        "mainapp/book_list.html",
        {
            "books": paginator.page(page),
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


@cache_page(3600)
def contacts(request):
    return render(request, "mainapp/contacts.html")
