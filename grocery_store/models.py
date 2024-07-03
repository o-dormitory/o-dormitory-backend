import uuid

from django.db import models


class GroceryImage(models.Model):
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
