from django.views.generic import ListView, CreateView, UpdateView, DetailView
from core.models import Price
from .base import LoginRequiredMixin

class PriceListView(LoginRequiredMixin, ListView):
    model = Price 
    template_name = "price_list/price_list.html"
    context_object_name = "price_list"

class PriceCreateView(LoginRequiredMixin, CreateView):
    model = Price
    template_name = "price_list/price_create.html"
    success_url = "/price"
    fields = ["name", "price"]

class PriceUpdateView(LoginRequiredMixin, UpdateView):
    model = Price
    template_name = "price_list/price_update.html"
    fields = ["name", "price"]
    success_url = "/price"

class PriceDetailView(LoginRequiredMixin, DetailView):
    model = Price
    template_name = "price_list/price_detail.html"
    context_object_name = "price"
