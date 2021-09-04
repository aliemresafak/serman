from django.contrib.auth import mixins

class LoginRequiredMixin(mixins.LoginRequiredMixin):
    login_url = "/auth/login"
    redirect_field_name = "redirect_to"
