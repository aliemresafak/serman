from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_field_name = "home"


class CustomLogoutView(LogoutView):
    template_name = None
