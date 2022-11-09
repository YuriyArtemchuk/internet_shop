from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


class Producer(models.Model):

    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):

    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(max_length=500, null=False)
    price = models.FloatField(null=False, default=0.00)
    first_price = models.FloatField(null=False, default=0.00)
    quantity = models.IntegerField(null=False, default=0)
    photo = models.FileField(upload_to='products/', null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)


