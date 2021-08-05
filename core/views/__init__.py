from typing import Any, Dict
from django.views.generic import TemplateView
from .user import *
from .price_list import *
from .service import *
from ..models import Service


class DashboardView(TemplateView):
    template_name = "dashboard.html"


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["sum_price"] = 0 

        for service in Service.objects.all():
            context["sum_price"] += service.price.price
        return context

