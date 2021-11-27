from django.forms import Form
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AuthForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)