from django.contrib import admin
from core.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "created_at")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("user", "number", "information", "price")


@admin.register(Price)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "amount")