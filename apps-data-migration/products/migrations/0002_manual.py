from django.db import migrations

# カテゴリ追加
INSERT_CATEGORIES_SQL = '''
INSERT INTO products_category (name)
VALUES
  (%s),
  (%s),
  (%s)
;
'''

# すべての値を削除
DELETE_CATEGORIES_SQL = '''
DELETE FROM products_category;
'''


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            [
                (INSERT_CATEGORIES_SQL, ('a', 'b', 'c',)),
                (INSERT_CATEGORIES_SQL, ('d', 'e', 'f',)),
            ], 
            DELETE_CATEGORIES_SQL
        ),
    ]
