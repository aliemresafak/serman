from django.db import models
from core.models import CommonField

class User(CommonField):
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    telephone_number = models.CharField(max_length=11, default="00000000000")

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"