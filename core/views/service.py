from django.db.models import F
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from core.models import Service, User, Price
from .base import LoginRequiredMixin

class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = "service/service_list.html"
    context_object_name = "service_list"

class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = "service/service_create.html"
    success_url = "/service"
    fields = ["user", "sim_lock_password", "phone_lock_password", "price"]
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        context["price_list"] = Price.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        price = Price.objects.filter(pk__in=request.POST.get("price"))
        price.update(amount=F("amount") - 1)
        return super().post(request, *args, **kwargs)


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    template_name = "service/service_update.html"
    success_url = "/service"
    slug_field = "number"
    fields = ["status"]

    context_object_name = "status_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status_list"] = Service.STATUS_CHOICES
        return context

class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service
    template_name = "service/service_detail.html"
    context_object_name = "service"
    slug_field = "number"

