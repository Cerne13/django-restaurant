from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.DecimalField()

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    price = models.DecimalField()
    dish_type = models.ForeignKey(
        to=DishType,
        on_delete=models.CASCADE,
        related_name="dish_type",
    )
    cooks = models.ManyToManyField(
        to=Cook,
        related_name="dish",
    )

    def __str__(self):
        return f"{self.name}: {self.price} USD"
