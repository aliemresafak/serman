from typing import Any, Dict
from django.views.generic import TemplateView
from datetime import datetime
from core.models import Service
from .base import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    login_url = "/auth/login/"
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["daily_repair_all"] = Service.objects.all().filter(created_at__day=datetime.now().day)

        context["daily_repair_waiting"] = Service.objects.filter(status=Service.WAITING, created_at__day=datetime.now().day)
        context["daily_repair_fixing"] = Service.objects.filter(status=Service.FIXING, created_at__day=datetime.now().day)
        context["daily_repair_fixed"] = Service.objects.filter(status=Service.FIXED, created_at__day=datetime.now().day)

        context["not_completed_fixing"] = Service.objects.filter(created_at__day__lt=datetime.now().day).exclude(status__exact=Service.FIXED)

        return context 
