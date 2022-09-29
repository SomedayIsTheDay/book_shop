from django.urls import path
import ordersapp.views as ordersapp

app_name = "ordersapp"

urlpatterns = [
    path("", ordersapp.OrderListView.as_view(), name="orders"),
    path("create/", ordersapp.create, name="create"),
    path("cancel/<int:pk>/", ordersapp.cancel, name="cancel"),
    path("<int:pk>/", ordersapp.OrderDetailView.as_view(), name="detail"),
]
