from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(LoginRequiredMixin):
    login_url = "/auth/login"
    redirect_field_name = "redirect_to"