from rest_framework import serializers

from grocery_store.models import GroceryStore


class GroceryStoreSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)

    class Meta:
        model = GroceryStore
        fields = [
            "uid",
            "name",
            "address",
        ]
