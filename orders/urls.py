from django.urls import path, re_path
from .views import order, confirm, ajax_delivery_info, success, failed

urlpatterns = [
    re_path(r'^order/(?P<sel_list>[0-9\,]+)$', order),
    re_path(r'^confirm/(?P<init_list>[0-9\,]+)/(?P<order_id>[0-9\,]+)$', confirm),
    path('ajax_delivery_info', ajax_delivery_info),
    path('success', success),
    path('failed', failed),
    
]
