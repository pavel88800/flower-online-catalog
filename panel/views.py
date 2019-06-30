from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from .forms import CategoryForm, SubCategoryForm
from .utils import *
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class IndexPage(LoginRequiredMixin, ObjectListMixin, View):
    model = Category()
    template = 'panel/base/index.html'


class CategoryList(LoginRequiredMixin, ObjectListMixin, View):
    model = Category()
    template = 'panel/other_templates/category/category_list.html'


class CategoryCreate(LoginRequiredMixin, ObjectsCreateUpdateMixin, View):
    form = CategoryForm
    template = 'panel/other_templates/category/category_create.html'
    where_redirect = '/panel/category/list/'


class CategoryUpdate(LoginRequiredMixin, ObjectsCreateUpdateMixin, View):
    form = CategoryForm
    template = 'panel/other_templates/category/category_update.html'
    where_redirect = '/panel/category/list/'
    model = Category()


class CategoryDelete(LoginRequiredMixin, ObjectsDelete, View):
    model = Category()


class SubCategoryList(LoginRequiredMixin, View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        categories = Category.objects.all()
        context = {
            'cat': category,
            'category': categories,
        }
        return render(request, 'panel/other_templates/sub_category/sub_category_list.html', context)


class SubCategoriesCreate(LoginRequiredMixin, ObjectsSubCreateUpdateMixin, View):
    form = SubCategoryForm
    template = 'panel/other_templates/sub_category/sub_category_create.html'
    where_redirect = '/panel/category/list/'


class SubCategoryUpdate(LoginRequiredMixin, ObjectsSubCreateUpdateMixin, View):
    form = SubCategoryForm
    template = 'panel/other_templates/sub_category/sub_category_update.html'
    where_redirect = '/panel/category/list/'
    model = SubCategory()


class SubCategoryDelete(LoginRequiredMixin, ObjectsDelete, View):
    model = SubCategory()


class CatalogItemList(LoginRequiredMixin, View):
    def get(self, request, sub_category_id):
        sub_category = SubCategory.objects.get(id=sub_category_id)
        all_categories = Category.objects.all()
        context = {
            'category': all_categories,
            'cat': sub_category,
        }
        return render(request, 'panel/other_templates/catalog_items/catalog_item_list.html', context)


class CatalogItemAllList(LoginRequiredMixin, View):
    def get(self, request):
        all_categories = Category.objects.all()
        catalog_items = Product.objects.all()
        paginator = Paginator(catalog_items, 10)
        page = request.GET.get('page', 1)
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)

        context = {
            'category': all_categories,
            'catalog_items': blog_list,
        }
        return render(request, 'panel/other_templates/catalog_items/catalog_item_all_list.html', context)


class CatalogItemCreate(LoginRequiredMixin, ObjectsCreateUpdateCatalogItem, View):
    model1 = Category()
    template = 'panel/other_templates/catalog_items/catalog_item_create.html'


class CatalogItemUpdate(LoginRequiredMixin, ObjectsCreateUpdateCatalogItem, View):
    model1 = Category()
    model2 = Product()
    template = 'panel/other_templates/catalog_items/catalog_item_update.html'


class CatalogItemDelete(LoginRequiredMixin, ObjectsDelete, View):
    model = Product()


def get_subcaegories(request):
    if request.is_ajax():
        categories = Category.objects.get(id=request.POST.get('id'))
        serialize = serializers.serialize('json', categories.subcategory_set.all())
        return HttpResponse(serialize, content_type="application/json")
