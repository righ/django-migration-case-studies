from django.db import migrations
from django.db.models import Func, F


def set_categories_uppercase(apps, schema_editor):
    Category = apps.get_model("products", "Category")
    Category.objects.all().update(
        name=Func(F('name'), function='UPPER')
    )


def set_categories_lowercase(apps, schema_editor):
    Category = apps.get_model("products", "Category")
    Category.objects.all().update(
        name=Func(F('name'), function='LOWER')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_manual'),
    ]

    operations = [
        migrations.RunPython(set_categories_uppercase, set_categories_lowercase)
    ]
