from django.urls import path, include
from .views import *
urlpatterns = [
    path('', MainPage.as_view()),
]
