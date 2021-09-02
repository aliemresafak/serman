from django.urls import path
from .views import *

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path("customer/", UserListView.as_view(), name="customer_list"),
    path("customer/create", UserCreateView.as_view(), name="customer_create"),
    path("customer/<pk>", UserDetailView.as_view(), name="customer_detail"),
    path("customer/<pk>/update", UserUpdateView.as_view(), name="customer_update"),
    path("price/", PriceListView.as_view(), name="price_list"),
    path("price/create", PriceCreateView.as_view(), name="price_create"),
    path("price/<pk>", PriceDetailView.as_view(), name="price_detail"),
    path("price/<pk>/update", PriceUpdateView.as_view(), name="price_update"),
    path("service/", ServiceListView.as_view(), name="service_list"),
    path("service/create/", ServiceCreateView.as_view(), name="service_create"),
    path("service/<slug:slug>", ServiceDetailView.as_view(), name="service_detail"),
    path(
        "service/<slug:slug>/update", ServiceUpdateView.as_view(), name="service_update"
    ),
    path("auth/login/", CustomLoginView.as_view(), name="login"),
    path("auth/logout/", CustomLogoutView.as_view(), name="logout"),
]
