from django.urls import path
from .views import CatalogHome, CategoriesHome, ProducersHome, product_detail, ajax_cart_product_page

urlpatterns = [
    # path('index', index, name='index'),
    path('index', CatalogHome.as_view(), name='catalog'),
    path('<int:cat_id>/', CategoriesHome.as_view(), name='category'),
    # path('<int:cat_id>/', categories, name='category'),
    # path('brand/<int:prod_id>/', producers, name='brand'),
    path('brand/<int:prod_id>/', ProducersHome.as_view(), name='brand'),
    path('product/<int:prod_id>/', product_detail, name='product'),
    # path('ajax_sort_catalog', ajax_sort_catalog, name='ajax_sort_catalog')
    path('ajax_cart_product_page', ajax_cart_product_page)
]

