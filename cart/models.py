from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product
from django.utils import timezone


class CartItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty_in_cart = models.IntegerField(default=1)
    total_price_in_cart = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(null=False, default=timezone.now)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} / {self.product} :: {self.date} - {self.qty_in_cart} - {self.total_price_in_cart} '
    
    def save(self, *args, **kwargs):
        self.total_price_in_cart = self.qty_in_cart * self.product.price

        super(CartItem, self).save(*args, **kwargs)