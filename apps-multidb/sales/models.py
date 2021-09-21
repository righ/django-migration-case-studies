from django.db import models
from django.utils import timezone


class Sales(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    sold_at = models.DateTimeField(default=timezone.now)


class Summary(models.Model):
    date = models.DateField()
    total_sales = models.IntegerField()
    total_price = models.IntegerField()
    unique_user = models.IntegerField()
