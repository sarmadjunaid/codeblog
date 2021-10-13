from django.urls import path

from .views import *

urlpatterns = [
    path('', frontpage, name='front_page'),
    path('<slug:slug>/', detail, name='detail'),
    path('category/<slug:slug>', category, name='category'),
]