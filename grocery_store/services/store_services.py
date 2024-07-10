from uuid import UUID
from grocery_store.models import GroceryStore
from grocery_store.serializers import GroceryStoreSerializer


class GroceryStoreService:
    @classmethod
    def get_all_stores(cls) -> GroceryStoreSerializer:
        stores = GroceryStore.objects.all()
        return GroceryStoreSerializer(stores, many=True)

    @classmethod
    def create_store(cls, name: str, address: str) -> GroceryStoreSerializer:
        serializer = GroceryStoreSerializer(data={
            "name": name,
            "address": address
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer

    @classmethod
    def get_store_by_uid(cls, uid: UUID) -> GroceryStoreSerializer:
        store = GroceryStore.objects.get(uid=uid)
        return GroceryStoreSerializer(store)

    @classmethod
    def update_store_by_uid(
        cls,
        uid: UUID,
        name: str,
        address: str,
    ) -> GroceryStoreSerializer:
        store = GroceryStore.objects.get(uid=uid)
        serializer = GroceryStoreSerializer(
            instance=store,
            data={"name": name, "address": address},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer

    @classmethod
    def delete_store_by_uid(cls, uid: UUID) -> None:
        store = GroceryStore.objects.get(uid=uid)
        store.delete()
