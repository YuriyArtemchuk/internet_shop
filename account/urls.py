from django.urls import path
from .views import *

urlpatterns = [
    path('reg', reg),
    path('entry', entry),
    path('confirm', confirm),
    path('exit', exit),
    path('profile', profile),
    path('reset', reset),
    path('reg_res', reg_res),
    path('entry_res', entry_res),
    path('ajax_signup', ajax_signup),
    path('ajax_email', ajax_email),
]
