from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class MainPage(View):
    def get(self, request):
        return render(request,'public/base/base.html',{'hellow':'hellow'})
