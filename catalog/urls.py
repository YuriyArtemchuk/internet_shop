from django.urls import path
from .views import index, ajax_sort_catalog

urlpatterns = [
    path('index', index, name='index'),
    path('ajax_sort_catalog', ajax_sort_catalog, name='ajax_sort_catalog')
]
