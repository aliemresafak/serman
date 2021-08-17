from django.db import models
from uuid import uuid4

class CommonField(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)

    class Meta:
        abstract = True

class User(CommonField):
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    telephone_number = models.CharField(max_length=11, default="00000000000")

    def __str__(self) -> str:
        return f"{self.name} {self.surname} {self.identity_number}"

def generate_uuid() -> str:
    uuid_arr = str(uuid4()).split("-")
    code = ""
    for i in uuid_arr:
        code += i[:2]
    return code

class Price(CommonField):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name}"

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

    def __st__(self) -> str:
        return f"{self.user.name}"

# class Service(CommonField):
#     name = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.name
