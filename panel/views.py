from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from .forms import CategoryForm, SubCategoryForm
from .utils import *
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.core import serializers


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


class CatalogItemCreate(View):
    def get(self, request):
        all_categories = Category.objects.all()
        context = {
            'category': all_categories
        }
        return render(request, 'panel/other_templates/catalog_items/catalog_item_create.html', context)

    def post(self, request):
        if request.method == 'POST':
            item = Product()
            item.name = request.POST.get('name')
            if request.POST.get('active'):
                item.active = True
            else:
                item.active = False
            category = Category.objects.get(id=request.POST.get('category'))
            print(category)
            item.category = category
            sub_category = SubCategory.objects.get(id=request.POST.get('sub_category'))
            item.sub_category = sub_category
            item.slug = request.POST.get('slug')
            item.description = request.POST.get('description')
            if request.FILES.get('prev_img'):
                item.prev_img = request.FILES.get('prev_img')
            item.price = request.POST.get('price')
            if request.POST.get('share'):
                item.share = True
            else:
                item.share = False

            if request.POST.get('new'):
                item.new = True
            else:
                item.new = False
            item.save()

            if request.FILES.get('img[]'):
                for image in request.FILES.getlist('img[]'):
                    img = Images()
                    img.img = image
                    img.product = Product.objects.get(slug=request.POST.get('slug'))
                    img.save()

            return redirect('/panel/')


def get_subcaegories(request):
    if request.is_ajax():
        categories = Category.objects.get(id=request.POST.get('id'))
        serialize = serializers.serialize('json', categories.subcategory_set.all())
        return HttpResponse(serialize, content_type="application/json")
