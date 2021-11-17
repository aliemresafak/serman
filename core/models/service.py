from uuid import uuid4
from django.db import models
from core.models import CommonField, User, Price
def generate_uuid() -> str:
    uuid_arr = str(uuid4()).split("-")
    code = ""
    for i in uuid_arr:
        code += i[:2]
    return code

class Service(CommonField):
    WAITING = "Tamir Bekliyor"
    FIXING = "Tamir Ediliyor"
    FIXED = "Tamir Edildi"
    STATUS_CHOICES = [
        (WAITING, WAITING),
        (FIXING, FIXING),
        (FIXED, FIXED)
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, auto_created=True, default=generate_uuid, editable=False)
    information = models.TextField()
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    status =models.CharField(choices=STATUS_CHOICES, max_length=14, default=WAITING)

    def __str__(self) -> str:
        return self.user.name