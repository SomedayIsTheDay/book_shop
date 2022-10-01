from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .models import BookUser
from .forms import BookUserRegistrationForm, BookUserLoginForm, BookUserEditForm


class BookUserCreateView(CreateView):
    template_name = "authapp/registration.html"
    model = BookUser
    form_class = BookUserRegistrationForm
    success_url = reverse_lazy("auth:login")


class BookUserLoginView(LoginView):
    template_name = "authapp/login.html"
    authentication_form = BookUserLoginForm
    extra_context = {"title": "Login"}


class BookUserEditView(LoginRequiredMixin, UpdateView):
    template_name = "authapp/edit.html"
    model = BookUser
    form_class = BookUserEditForm

    def get_success_url(self):
        user_pk = self.kwargs["pk"]
        return reverse_lazy("auth:edit", args=[user_pk])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.GET.get("next") and "/cart/" in self.request.GET.get("next"):
            data["message"] = messages.info(
                self.request,
                "You need to fill the geolocation fields before making an order",
            )
        return data


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("auth:login"))
