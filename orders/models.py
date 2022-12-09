from django.db import models
from cart.models import CartItem
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(null=False, default=0.00)
    date_order = models.DateTimeField(null=False, default=timezone.now)
    date_confirm = models.DateTimeField(null=True)
    status = models.CharField(max_length=256)

    def __str__(self) -> str:
        return str(self.user)


class Purchase(models.Model):

    cart_items = models.ForeignKey(CartItem, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.order)


class Delivery(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=256, null=False)
    city = models.CharField(max_length=256, null=False)
    depot = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null=True)
    note = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.user} / {self.order} :: {self.phone} :: {self.company} : {self.city}'

