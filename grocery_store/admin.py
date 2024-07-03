from django.contrib import admin
from .models import GroceryImage


@admin.register(GroceryImage)
class GroceryImageAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "file_name",
    )
