from django.db import migrations

SQL = """
UPDATE products_product AS p
SET category_id2 = (
  SELECT id2
  FROM products_category AS c
  WHERE p.category_id = c.id
)
;
"""


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_id2'),
    ]

    operations = [
        migrations.RunSQL(SQL),
    ]
