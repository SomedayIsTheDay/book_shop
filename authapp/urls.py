from django.urls import path
import authapp.views as authapp

app_name = "authapp"

urlpatterns = [
    path("login/", authapp.BookUserLoginView.as_view(), name="login"),
    path("logout/", authapp.logout, name="logout"),
    path("edit/<int:pk>/", authapp.BookUserEditView.as_view(), name="edit"),
    path(
        "register/",
        authapp.BookUserCreateView.as_view(),
        name="registration",
    ),
]
