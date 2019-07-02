from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from .forms import *
from .utils import *
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import logout


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


class StaticPageAllList(LoginRequiredMixin, View):
    def get(self, request):
        pages = StaticPage.objects.all()
        all_categories = Category.objects.all()

        context = {
            'category': all_categories,
            'pages': pages,
        }
        return render(request, 'panel/other_templates/static_pages/static_pages_all_list.html', context)


class StaticPageCreate(LoginRequiredMixin, View):
    def get(self, request):
        all_categories = Category.objects.all()
        form = StaticPageForm()

        context = {
            'category': all_categories,
            'form': form,
        }
        return render(request, 'panel/other_templates/static_pages/static_pages_create.html', context)

    def post(self, request):
        form = StaticPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/panel/static_page/all_list/')
        return render(request, 'panel/other_templates/static_pages/static_pages_create.html', {'form': form})


class StaticPageUpdate(LoginRequiredMixin, View):
    def get(self, request, page_id):
        page = StaticPage.objects.get(id=page_id)
        all_categories = Category.objects.all()
        form = StaticPageForm(instance=page)
        pages = StaticPage.objects.all()

        context = {
            'category': all_categories,
            'form': form,
            'pages': pages,
            'page': page,
        }
        return render(request, 'panel/other_templates/static_pages/static_pages_update.html', context)

    def post(self, request, page_id):
        page = StaticPage.objects.get(id=page_id)
        bound_form = StaticPageForm(request.POST, instance=page)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('/panel/static_page/all_list/')
        return render(request, 'panel/other_templates/static_pages/static_pages_update.html', context)


class StaticPageDelete(LoginRequiredMixin, ObjectsDelete, View):
    model = StaticPage()


class TagsList(View):
    def get(self, request):
        all_categories = Category.objects.all()
        tags = Tags.objects.all()
        paginator = Paginator(tags, 10)
        page = request.GET.get('page', 1)
        try:
            tags = paginator.page(page)
        except PageNotAnInteger:
            tags = paginator.page(1)
        except EmptyPage:
            tags = paginator.page(paginator.num_pages)

        context = {
            'category': all_categories,
            'tags': tags,
        }
        return render(request, 'panel/other_templates/tags/tags_list.html', context)


class TagsCreate(View):
    def get(self, request):
        all_categories = Category.objects.all()
        form = TagsForm()
        context = {
            'category': all_categories,
            'form': form,
        }
        return render(request, 'panel/other_templates/tags/tags_create.html', context)

    def post(self, request):
        form = TagsForm(request.POST)
        all_categories = Category.objects.all()

        if form.is_valid():
            form.save()
            return redirect('/panel/tags/list/')
        context = {
            'category': all_categories,
            'form': form,
        }
        return render(request, 'panel/other_templates/tags/tags_create.html', context)


class TagsUpdate(View):
    def get(self, request, tag_id):
        tag = Tags.objects.get(id=tag_id)
        form = TagsForm(instance=tag)
        all_categories = Category.objects.all()
        context = {
            'category': all_categories,
            'form': form,
            'tag': tag,
        }
        return render(request, 'panel/other_templates/tags/tags_update.html', context)

    def post(self, request, tag_id):
        tag = Tags.objects.get(id=tag_id)
        bound_form = TagsForm(request.POST, instance=tag)
        all_categories = Category.objects.all()
        if bound_form.is_valid():
            bound_form.save()
            return redirect('/panel/tags/list/')
        context = {
            'category': all_categories,
            'form': bound_form,
            'tag': tag,
        }
        return render(request, 'panel/other_templates/tags/tags_update.html', context)


class TagItemsList(LoginRequiredMixin, View):
    def get(self, request, tag_id):
        tag = Tags.objects.get(id=tag_id)
        all_categories = Category.objects.all()
        context = {
            'category': all_categories,
            'tag': tag,
        }
        return render(request, 'panel/other_templates/tags/tags_catalog_items_list.html', context)

class TagsDelete(ObjectsDelete, View):
    model = Tags()


class ArticleList(View):
    def get(self, request):
        all_categories = Category.objects.all()
        articles = Articles.objects.all()
        paginator = Paginator(articles, 10)
        page = request.GET.get('page', 1)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context = {
            'category': all_categories,
            'articles': articles,
        }
        return render(request, 'panel/other_templates/articles/articles_list.html', context)


class ArticleCreate(View):
    def get(self, request):
        all_categories = Category.objects.all()
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'panel/other_templates/articles/articles_create.html', context)

    def post(self, request):
        all_categories = Category.objects.all()
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/panel/')
        context = {
            'category': all_categories,
            'form': form,
        }
        return render(request, 'panel/other_templates/articles/articles_create.html', context)


class ArticleUpdate(View):
    def get(self, request, article_id):
        article = Articles.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        all_categories = Category.objects.all()
        context = {
            'category': all_categories,
            'form': form,
            'article': article,
        }
        return render(request, 'panel/other_templates/articles/articles_update.html', context)

    def post(self, request, article_id):
        all_categories = Category.objects.all()
        article = Articles.objects.get(id=article_id)
        bound_form = ArticleForm(request.POST, instance=article)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('/panel/')
        context = {
            'category': all_categories,
            'form': bound_form,
        }
        return render(request, 'panel/other_templates/articles/articles_update.html', context)


class ArticleDelete(LoginRequiredMixin, ObjectsDelete, View):
    model = Articles()


def logout_view(request):
    logout(request)
    return redirect('/admin/login/?next=/panel/')
