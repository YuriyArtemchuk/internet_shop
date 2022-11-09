from django.urls import path
from .views import *

urlpatterns = [
    path('ajax_cart', ajax_cart),
    path('ajax_cart_display', ajax_cart_display),
]
