from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "category",
            "description",
            "preparation_time",
            "cooking_time",
            "estimated_cost",
            "image",
            "tags",
            "ingredients",
            "private_notes",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "private_notes": forms.Textarea(attrs={"rows": 3}),
            "ingredients": forms.CheckboxSelectMultiple(),
            "tags": forms.TextInput(attrs={"placeholder": "vegan, sans-gluten, rapide"}),
            "image": forms.FileInput(attrs={"accept": "image/*"}),
        }
