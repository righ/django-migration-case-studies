from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_category_id2_to_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='products.Category'),
        ),
    ]
