from django.urls import path

from .views import *

urlpatterns = [
    path('', frontpage, name='front_page')
]