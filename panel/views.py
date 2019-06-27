from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from .forms import CategoryForm, SubCategoryForm
from .utils import *


class IndexPage(ObjectListMixin, View):
    model = Category()
    template = 'panel/base/index.html'


class CategoryList(ObjectListMixin, View):
    model = Category()
    template = 'panel/other_templates/category/category_list.html'


class CategoryCreate(ObjectsCreateUpdateMixin, View):
    form = CategoryForm
    template = 'panel/other_templates/category/category_create.html'
    where_redirect = '/panel/category/list/'


class CategoryUpdate(ObjectsCreateUpdateMixin, View):
    form = CategoryForm
    template = 'panel/other_templates/category/category_update.html'
    where_redirect = '/panel/category/list/'
    model = Category()


class CategoryDelete(ObjectsDelete, View):
    model = Category()


class SubCategoryList(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        categories = Category.objects.all()
        context = {
            'cat': category,
            'category': categories,
        }
        return render(request, 'panel/other_templates/sub_category/sub_category_list.html', context)


class SubCategoriesCreate(ObjectsSubCreateUpdateMixin, View):
    form = SubCategoryForm
    template = 'panel/other_templates/sub_category/sub_category_create.html'
    where_redirect = '/panel/category/list/'


class SubCategoryUpdate(ObjectsSubCreateUpdateMixin, View):
    form = SubCategoryForm
    template = 'panel/other_templates/sub_category/sub_category_update.html'
    where_redirect = '/panel/category/list/'
    model = SubCategory()


class SubCategoryDelete(ObjectsDelete, View):
    model = SubCategory()
