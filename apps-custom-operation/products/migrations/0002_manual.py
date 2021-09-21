from django.db import migrations
from django.db.migrations.operations.base import Operation


class CreateCategory(Operation):
    reversible = True

    def __init__(self, name):
        self.name = name

    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        schema_editor.execute("INSERT INTO products_category (name) VALUES (%s);", (self.name,))

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        schema_editor.execute("DELETE FROM products_category WHERE name=%s;", (self.name,))

    def describe(self):
        return "Creates category %s" % self.name


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        CreateCategory('alpaca'),
        CreateCategory('dog'),
    ]
