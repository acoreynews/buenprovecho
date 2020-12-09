from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Recipe, Author, Type_of_food

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'slug', 'photo', 'author', 'summary', 'ingredients', 'instructions', 'type_of_food')


    widgets = {
        'name':forms.TextInput(attrs={'class': 'form-control'}),
        'slug':forms.TextInput(attrs={'class': 'form-control'}),
        'photo':forms.ImageField(),
        'author':forms.Select(attrs={'class': 'form-control'}),
        'summary':forms.Textarea(attrs={'class': 'form-control'}),
        'ingredients':forms.Textarea(attrs={'class': 'form-control'}),
        'instructions':forms.Textarea(attrs={'class': 'form-control'}),
        'type_of_food':forms.TextInput(attrs={'class': 'form-control'}),
    }
