from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_id2_primary_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='id2',
            new_name='id',
        ),
    ]
