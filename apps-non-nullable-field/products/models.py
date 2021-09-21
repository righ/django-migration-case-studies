from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField()

