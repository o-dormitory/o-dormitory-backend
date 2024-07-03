from django.contrib import admin
from .models import GroceryImage, GroceryCard, GroceryStore, CardInGroceryStore


@admin.register(CardInGroceryStore)
class CardInGroceryStoreAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "card",
        "store",
        "price",
        "remaining",
    )
    list_filter = (
        "card",
        "store",
    )


@admin.register(GroceryStore)
class GroceryStoreAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "name",
        "address",
    )


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
