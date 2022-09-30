from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    genre = models.ForeignKey(Genre, related_name="genre", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to="books_images")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author, related_name="authors")

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
