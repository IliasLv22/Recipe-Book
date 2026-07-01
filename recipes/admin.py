from django.contrib import admin
from .models import Category, Ingredient, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    search_fields = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)

    search_fields = ("name",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "preparation_time",
        "created_at",
    )

    list_filter = (
        "category",
        "author",
    )

    search_fields = (
        "title",
        "author__username",
    )

    filter_horizontal = ("ingredients",)

    ordering = (
        "-created_at",
    )