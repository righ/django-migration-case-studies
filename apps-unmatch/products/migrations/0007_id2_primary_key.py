from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_del_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='id2',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
