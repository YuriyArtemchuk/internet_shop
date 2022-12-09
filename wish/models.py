from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product
from django.utils import timezone


class WishItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return f'{self.user} / {self.product} :: {self.date}'
