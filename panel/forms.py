from .models import *
from django import forms
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control category-title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control category-slug'}),
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['title', 'slug', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control sub-category-title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control sub-category-slug'}),
            'category': forms.Select(attrs={'class': 'form-control sub-category-items'}),
        }
