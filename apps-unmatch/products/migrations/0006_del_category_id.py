from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_put_new_pk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
