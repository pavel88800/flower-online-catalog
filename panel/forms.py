from .models import *
from django import forms
from django.core.exceptions import ValidationError
import datetime


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


class StaticPageForm(forms.ModelForm):
    class Meta:
        model = StaticPage
        fields = ['title', 'slug', 'det_text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control sub-category-title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control sub-category-slug'}),
            'det_text': forms.Textarea(attrs={'class': 'form-control sub-category-items', 'id': 'description_product'}),
        }


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control sub-category-title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control sub-category-slug'}),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'slug', 'tags', 'catalog_items', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control sub-category-title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control sub-category-slug'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'catalog_items': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'description_product'}),

        }
