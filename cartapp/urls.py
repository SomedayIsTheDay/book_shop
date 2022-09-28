from django.urls import path
import cartapp.views as cartapp

app_name = "cartapp"

urlpatterns = [
    path("", cartapp.cart, name="cart"),
    path("add/<int:pk>/", cartapp.add, name="add"),
    path("decrement/<int:pk>/", cartapp.decrement, name="decrement"),
    path("remove/<int:pk>/", cartapp.remove, name="remove"),
    path("edit/<int:pk>/<int:quantity>/", cartapp.edit, name="edit"),
]
