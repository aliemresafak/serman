from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Service
from .base import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    login_url = "/auth/login/"
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.all()
        context["daily_repair_all"] = services.filter(created_at__day=datetime.now().day)

        context["daily_repair_waiting"] = services.filter(status=Service.WAITING, created_at__day=datetime.now().day)
        context["daily_repair_fixing"] = services.filter(status=Service.FIXING, created_at__day=datetime.now().day)
        context["daily_repair_fixed"] = services.filter(status=Service.FIXED, created_at__day=datetime.now().day)

        context["not_completed_fixing"] = services.filter(created_at__day__lt=datetime.now().day).exclude(status__exact=Service.FIXED)

        return context 

class ServiceStatusView(TemplateView):
    template_name = "service_status.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        service_objects = Service.objects.all()
        service_number = request.POST.get("service_number")

        data = service_objects.filter(number=service_number).first()

        if data:
            print(data)
            return render(request, self.template_name, {"data": data, "errors": "Bu servise numarasina ait kayit bulunamadi"})
        else:
            print(data)
            return render(request, self.template_name, {"data": data})