from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "year", "color", "price")
    search_fields = ("make", "model", "year", "color")
    list_filter = ("year", "color")
