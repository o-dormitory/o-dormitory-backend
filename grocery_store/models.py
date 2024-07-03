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
