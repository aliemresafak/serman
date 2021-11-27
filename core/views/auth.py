from django.contrib.auth.views import LoginView, LogoutView
from core.forms import AuthForm

class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_field_name = "home"
    form_class = AuthForm
    

    def form_valid(self, form):
        remember_me = form.cleaned_data["remember_me"]
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = "/"
