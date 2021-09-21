from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='effective_date_to',
            new_name='effective_date_end',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='effective_date_from',
            new_name='effective_date_start',
        ),
    ]
