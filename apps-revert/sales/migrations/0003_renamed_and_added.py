from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summary',
            old_name='total',
            new_name='total_price',
        ),
        migrations.AddField(
            model_name='summary',
            name='total_sales',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summary',
            name='unique_user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
