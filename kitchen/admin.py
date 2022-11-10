from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, DishType, Dish


@admin.register(Cook)
class CookAdmin(UserAdmin):
    search_fields = ("username", "email", "first_name", "last_name")
    list_display = UserAdmin.list_display + ("years_of_experience",)
    list_filter = ("username", "years_of_experience")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info",), {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "years_of_experience"
            )
        }),
        (
            ("Permissions",),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates",), {"fields": ("last_login", "date_joined")}),
    )


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("dish_type",)
