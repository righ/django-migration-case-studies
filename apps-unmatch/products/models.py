import uuid

from django.db import models
from django.utils import timezone


class Category(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    # id2 = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')
    # category_id2 = models.IntegerField(default=0)
    # category_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Price(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    effective_date_start = models.DateTimeField(null=True)
    effective_date_end = models.DateTimeField(null=True)
