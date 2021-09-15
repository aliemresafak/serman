from django.views.generic import ListView, DetailView, CreateView, UpdateView
from core.models import User
from .base import LoginRequiredMixin
user_fields = ["name", "surname", "telephone_number"]

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "customer/customer_list.html"
    context_object_name = "users"

class UserCreateView(LoginRequiredMixin,CreateView):
    model = User
    template_name = "customer/customer_create.html"
    success_url = "/customer"
    fields = user_fields

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "customer/customer_detail.html"
    context_object_name = "customer"
    slug_field = "pk"

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "customer/customer_update.html"
    success_url = "/customer"
    fields = user_fields
