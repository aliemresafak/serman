from django.urls import path
from .views import *

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path("users/", UserListView.as_view(), name="users"),
    path("users/create", UserCreateView.as_view(), name="user_create"),
    path("users/<pk>", UserDetailView.as_view(), name="user_detail"),
    path("users/<pk>/update", UserUpdateView.as_view(), name="user_update"),
    path("price/", PriceListView.as_view(), name="price_list"),
    path("price/create", PriceCreateView.as_view(), name="price_list_create"),
    path("price/<pk>", PriceDetailView.as_view(), name="price_detail"),
    path("price/<pk>/update", PriceUpdateView.as_view(), name="price_update"),

    path("service/", ServiceListView.as_view(), name="service_list"),
    path("service/create/", ServiceCreateView.as_view(), name="service_create"),
    path("service/<slug:slug>", ServiceDetailView.as_view(), name="service_detail"),
    path("service/<slug:slug>/update", ServiceUpdateView.as_view(), name="service_update")
]