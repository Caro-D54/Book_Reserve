from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ("mail", "name", "is_staff", "is_superuser")
    search_fields = ("mail", "name")
    ordering = ("mail",)

    fieldsets = (
        (None, {"fields": ("mail", "password")}),
        ("Información personal", {"fields": ("name",)}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas importantes", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("mail", "name", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

admin.site.register(User, CustomUserAdmin)
