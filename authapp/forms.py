from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from .models import BookUser
from django import forms


class BookUserRegistrationForm(UserCreationForm):
    class Meta:
        model = BookUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
            "age",
            "avatar",
        )

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 3:
            raise forms.ValidationError(
                "Your username must be at least 3 characters long"
            )
        return username


class BookUserEditForm(UserChangeForm):
    class Meta:
        model = BookUser
        fields = (
            "username",
            "first_name",
            "email",
            "age",
            "avatar",
        )

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 3:
            raise forms.ValidationError(
                "Your username must be at least 3 characters long"
            )
        return username


class BookUserLoginForm(AuthenticationForm):
    class Meta:
        model = BookUser
        fields = ("username", "password")
