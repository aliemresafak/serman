from django.db import models
from core.models import CommonField

class Price(CommonField):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.PositiveSmallIntegerField(null=False)

    def __str__(self) -> str:
        return self.name
