from typing import Any, Dict
from django.views.generic import TemplateView
from datetime import datetime
from core.models import Service

class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["daily_repair_all"] = Service.objects.all().filter(created_at__day=datetime.now().day)

        context["daily_repair_waiting"] = Service.objects.all().filter(status=Service.WAITING, created_at__day=datetime.now().day)
        context["daily_repair_fixing"] = Service.objects.all().filter(status=Service.FIXING, created_at__day=datetime.now().day)
        context["daily_repair_fixed"] = Service.objects.all().filter(status=Service.FIXED, created_at__day=datetime.now().day)

        return context 