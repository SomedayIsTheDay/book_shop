from django.urls import path
import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.books, name="index"),
    path("<int:page>/", mainapp.books, name="books"),
    path("book/<int:pk>/", mainapp.book, name="book"),
]
