from django.contrib import admin
from .models import Order, Purchase, Delivery


admin.site.register(Order)
admin.site.register(Purchase)
admin.site.register(Delivery)

