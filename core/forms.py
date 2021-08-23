from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import User

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ["name","surname", "telephone_number"]