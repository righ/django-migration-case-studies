from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_id2_to_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id2',
            new_name='category_id',
        ),
    ]
