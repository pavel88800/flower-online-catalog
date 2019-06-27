from django.shortcuts import render, redirect, get_object_or_404
from .models import *


class ObjectListMixin:
    model = None
    template = None

    def get(self, request):
        obj = self.model.__class__.objects.all()
        context = {
            self.model.__class__.__name__.lower(): obj,
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


class ObjectsDelete:
    model = None

    def get(self, request, sub_category_id=0, category_id=0):
        if sub_category_id != 0:
            obj =  get_object_or_404(self.model.__class__, id=sub_category_id).delete()
        if category_id != 0:
            obj =  get_object_or_404(self.model.__class__, id=category_id).delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
