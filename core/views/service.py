from typing import Any, Dict
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from core.models import Service, User, Price


class ServiceListView(ListView):
    model = Service
    template_name = "service/service_list.html"
    context_object_name = "service_list"

class ServiceCreateView(CreateView):
    model = Service
    template_name = "service/service_create.html"
    success_url = "/service"
    fields = ["user", "information", "price"]
    context_object_name = "form"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["errors"] = list()
        if User.objects.all().count() == 0:
            context["errors"].append("Lütfen müşteri kaydı yapınız")
        else:
            context["users"] = User.objects.all()
        if Price.objects.all().count() == 0:
            context["errors"].append("Lütfen fiyat kaydı giriniz")
        else:
            context["price_list"] = Price.objects.all()
        return context


class ServiceUpdateView(UpdateView):
    model = Service
    template_name = "service/service_update.html"
    success_url = "/service"
    slug_field = "number"
    fields = ["status"]

class ServiceDetailView(DetailView):
    model = Service
    template_name = "service/service_detail.html"
    context_object_name = "service"
    slug_field = "number"

