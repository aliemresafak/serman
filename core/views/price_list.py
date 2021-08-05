from typing import List
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from core.models import Price

class PriceListView(ListView):
    model = Price 
    template_name = "price_list/price_list.html"
    context_object_name = "price_list"

class PriceCreateView(CreateView):
    model = Price
    template_name = "price_list/price_create.html"
    success_url = "/price"
    fields = ["name", "price"]

class PriceUpdateView(UpdateView):
    model = Price
    template_name = "price_list/price_update.html"
    fields = ["name", "price"]
    success_url = "/price"

class PriceDetailView(DetailView):
    model = Price
    template_name = "price_list/price_detail.html"
    context_object_name = "price"