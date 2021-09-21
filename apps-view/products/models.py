from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30)


class DoubleCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'double_category'
        managed = False
