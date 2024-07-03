from django.contrib import admin
from .models import GroceryImage, GroceryCard


@admin.register(GroceryCard)
class GroceryCardAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "name",
    )


@admin.register(GroceryImage)
class GroceryImageAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "file_name",
    )
