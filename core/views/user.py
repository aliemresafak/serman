from django.views.generic import ListView, DetailView, CreateView, UpdateView
from core.models import User

user_fields = ["name", "surname", "identity_number", "telephone_number"]

class UserListView(ListView):
    model = User
    template_name = "user/users.html"
    context_object_name = "users"

class UserCreateView(CreateView):
    model = User
    template_name = "user/user_create.html"
    success_url = "/users"
    fields = user_fields

class UserDetailView(DetailView):
    model = User
    template_name = "user/user_detail.html"
    context_object_name = "user"
    slug_field = "pk"

class UserUpdateView(UpdateView):
    model = User
    template_name = "user/user_update.html"
    success_url = "/users"
    fields = user_fields