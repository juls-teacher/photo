
from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "created_at")
    fields = ("title", "image", "price", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")