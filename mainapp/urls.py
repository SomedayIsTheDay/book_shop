from django.urls import path
import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.books, name="index"),
    path("<int:pk>/", mainapp.book, name="book"),
]
