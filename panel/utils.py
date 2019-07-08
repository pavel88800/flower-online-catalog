from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator


class ObjectListMixin:
    model = None
    template = None

    def get(self, request):
        obj = self.model.__class__.objects.all()
        pages = StaticPage.objects.all()
        context = {
            'category': obj,
            'pages': pages,
        }
        return render(request, self.template, context)


class ObjectsCreateUpdateMixin:
    model = None
    form = None
    template = None
    where_redirect = None

    def get(self, request, category_id=0):
        prev_page = request.META.get('HTTP_REFERER', '/')
        if self.model == None:
            form = self.form()
            all_categories = Category.objects.all()  # конченный костыль)
            return render(request, self.template, {'form': form, 'prev_page': prev_page, 'category': all_categories, })
        else:
            obj = get_object_or_404(self.model.__class__, id=category_id)
            all_categories = self.model.__class__.objects.all()
            form = self.form(instance=obj)
            return render(request, self.template,
                          {'form': form, 'cat': obj, 'category': all_categories, 'prev_page': prev_page})

    def post(self, request, category_id=0):
        prev_page = request.META.get('HTTP_REFERER', '/')
        if self.model == None:
            bound_form = self.form(request.POST)
            if bound_form.is_valid():
                bound_form.save()
                return redirect(self.where_redirect)
            return render(request, self.template, {'form': bound_form, 'prev_page': prev_page})
        else:
            category = get_object_or_404(self.model.__class__, id=category_id)
            bound_form = self.form(request.POST, instance=category)
            all_categories = self.model.__class__.objects.all()
            if bound_form.is_valid():
                bound_form.save()
                return redirect(self.where_redirect)
            return render(request, self.template,
                          {'form': bound_form, 'cat': category, 'category': all_categories, 'prev_page': prev_page})


class ObjectsSubCreateUpdateMixin:
    model = None
    form = None
    template = None
    where_redirect = None

    def get(self, request, sub_category_id=0):
        prev_page = request.META.get('HTTP_REFERER', '/')
        if self.model == None:
            form = self.form()
            all_categories = Category.objects.all()  # конченный костыль)
            return render(request, self.template, {'form': form, 'prev_page': prev_page, 'category': all_categories, })
        else:
            print(sub_category_id)
            obj = get_object_or_404(self.model.__class__, id=sub_category_id)
            all_categories = Category.objects.all()
            form = self.form(instance=obj)
            return render(request, self.template,
                          {'form': form, 'cat': obj, 'category': all_categories, 'prev_page': prev_page})

    def post(self, request, sub_category_id=0):
        prev_page = request.META.get('HTTP_REFERER', '/')
        if self.model == None:
            bound_form = self.form(request.POST)
            if bound_form.is_valid():
                bound_form.save()
                return redirect(self.where_redirect)
            return render(request, self.template, {'form': bound_form, 'prev_page': prev_page})
        else:
            category = get_object_or_404(self.model.__class__, id=sub_category_id)
            bound_form = self.form(request.POST, instance=category)
            all_categories = Category.objects.all()
            if bound_form.is_valid():
                bound_form.save()
                return redirect(self.where_redirect)
            return render(request, self.template,
                          {'form': bound_form, 'cat': category, 'category': all_categories, 'prev_page': prev_page})


class ObjectsCreateUpdateCatalogItem:
    model1 = None
    model2 = None
    template = None

    def get(self, request, item_id=0):
        if item_id == 0:
            all_categories = self.model1.__class__.objects.all()
            context = {
                'category': all_categories
            }
            return render(request, self.template, context)
        else:
            item = self.model2.__class__.objects.get(id=item_id)
            all_categories = self.model1.__class__.objects.all()
            images = Images.objects.filter(product=item)
            context = {
                'category': all_categories,
                'item': item,
                'images': images,
            }
            return render(request, self.template, context)

    def post(self, request, item_id=0):
        if request.method == 'POST':
            if item_id == 0:
                item = Product()
            else:
                item = self.model2.__class__.objects.get(id=item_id)
            item.name = request.POST.get('name')
            if request.POST.get('active'):
                item.active = True
            else:
                item.active = False
            category = self.model1.__class__.objects.get(id=request.POST.get('category'))
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
            return redirect('/panel/catalog_item/')


class ObjectsDelete:
    model = None

    def get(self, request, sub_category_id=0, category_id=0, item_id=0,
            page_id=0, tag_id=0, article_id=0, review_id=0):  # Тут очень тупанул. Надо было один параметр задать и юзать везде его, не было бы такой херни в аргументах метода, но раз так начал делать, то буду продолжать
        if sub_category_id != 0:
            obj = get_object_or_404(self.model.__class__, id=sub_category_id).delete()
        if category_id != 0:
            obj = get_object_or_404(self.model.__class__, id=category_id).delete()
        if item_id != 0:
            obj = get_object_or_404(self.model.__class__, id=item_id).delete()
        if page_id != 0:
            obj = get_object_or_404(self.model.__class__, id=page_id).delete()
        if tag_id != 0:
            obj = get_object_or_404(self.model.__class__, id=tag_id).delete()
        if article_id != 0:
            obj = get_object_or_404(self.model.__class__, id=article_id).delete()
        if review_id != 0:
            obj = get_object_or_404(self.model.__class__, id=review_id).delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
