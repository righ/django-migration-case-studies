from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_put_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id2',
            field=models.IntegerField(default=0),
        ),
    ]
