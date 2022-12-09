from django.urls import path
from .views import *

urlpatterns = [
    path('ajax_wish', ajax_wish),
    path('ajax_wish_display', ajax_wish_display),
]

