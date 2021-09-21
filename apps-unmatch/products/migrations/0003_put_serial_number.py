from django.db import migrations

SQL = """
UPDATE products_category AS a
SET id2 = (
  SELECT COUNT(1) + 1
  FROM products_category AS b
  WHERE
    -- 登録日時が同じ場合に重複してしまうので name でソート
    (a.created_at = b.created_at AND a.name > b.name)
    -- それ以外の場合は 登録日時でソート
    OR a.created_at > b.created_at
);
"""


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_id2'),
    ]

    operations = [
        migrations.RunSQL(SQL)
    ]
