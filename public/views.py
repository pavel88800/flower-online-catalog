from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from panel.models import *


class MainPage(View):
    def get(self, request):
        all_categories = Category.objects.all()
        reviews = Reviews.objects.all()
        static_pages = StaticPage.objects.all()
        context = {
            'categories': all_categories,
            'reviews': reviews,
            'static_pages': static_pages,
        }
        return render(request, 'public/base/base.html', context)
