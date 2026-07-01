from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="recipes"
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    preparation_time = models.PositiveIntegerField(
        help_text="Temps en minutes"
    )

    ingredients = models.ManyToManyField(
        "Ingredient",
        related_name="recipes",
        blank=True,
    )

    image = models.ImageField(
        upload_to="recipes/",
        null=True,
        blank=True,
        help_text="Image de la recette"
    )

    cooking_time = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Durée de cuisson en minutes"
    )

    estimated_cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Coût estimé en euros"
    )

    tags = models.CharField(
        max_length=200,
        blank=True,
        help_text="Tags séparés par des virgules (ex: vegan, sans-gluten, rapide)"
    )

    private_notes = models.TextField(
        blank=True,
        help_text="Notes privées visibles uniquement par l'auteur"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
        ordering = ["name"]

    def __str__(self):
        return self.name