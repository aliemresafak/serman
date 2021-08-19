from typing import Any, Dict
# from datetime import datetime
# from django.views.generic import TemplateView
from .user import *
from .price_list import *
from .service import *
# from ..models import Service
from .dashboard import * 


# class DashboardView(TemplateView):
#     template_name = "dashboard.html"


#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)

#         context["sum_price_daily"] = sum([service.price.price for service in Service.objects.all().filter(created_at__day=datetime.now().day)])
#         context["sum_price_monthly"] = sum([service.price.price for service in Service.objects.all().filter(created_at__month=datetime.now().month)])

#         context["repair_waiting"] = Service.objects.all().filter(status=Service.WAITING)
#         context["repair_fixing"] = Service.objects.all().filter(status=Service.FIXING)
#         context["repair_fixed"] = Service.objects.all().filter(status=Service.FIXED)

#         return context

