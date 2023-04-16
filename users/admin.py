from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_superuser", "last_login")
    fields = ("email", "is_staff", "is_superuser", "last_login")
    search_fields = ("email",)