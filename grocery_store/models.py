import uuid

from django.db import models


class GroceryImage(models.Model):
    """Model for storing grocery card images"""
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    file_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.file_name}"

    class Meta:
        verbose_name = "Grocery Image"
        verbose_name_plural = "Grocery Images"
        db_table = "grocery_images"
        ordering = ["file_name"]


class GroceryCard(models.Model):
    """Model for storing grocery cards"""
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    # TODO: add default image and can be blank
    image = models.OneToOneField(
        to=GroceryImage,
        on_delete=models.CASCADE,
        related_name="grocery_image",
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Grocery Card"
        verbose_name_plural = "Grocery Cards"
        db_table = "grocery_cards"
        ordering = ["name"]


class GroceryStore(models.Model):
    """Model for storing grocery stores"""
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} - {self.address}"

    class Meta:
        verbose_name = "Grocery Store"
        verbose_name_plural = "Grocery Stores"
        db_table = "grocery_stores"
        ordering = ["name"]
        unique_together = ["name", "address"]


class CardInGroceryStore(models.Model):
    """Model for storing cards in grocery stores"""
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    card = models.ForeignKey(to=GroceryCard, on_delete=models.CASCADE)
    store = models.ForeignKey(to=GroceryStore, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    remaining = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.card.name} - {self.store.name}"

    class Meta:
        verbose_name = "Card In Grocery Store"
        verbose_name_plural = "Cards In Grocery Store"
        db_table = "card_in_grocery_stores"
        ordering = ["store", "card"]
        unique_together = ["card", "store"]
