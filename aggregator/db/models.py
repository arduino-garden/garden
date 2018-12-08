from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from db.constants import db_keyspace
import sys
import inspect


class Plant(Model):
    id = columns.UUID(primary_key=True)
    name = columns.Text()


__module_name = __name__


def all_models():
    current_module = sys.modules[__module_name]
    for name, obj in inspect.getmembers(current_module):
        if inspect.isclass(obj) and 'db.models' in str(obj):
            yield obj


def truncate_tables():
    for model in all_models():
        connection.execute('truncate ' + model.column_family_name())


def sync_all_tables():
    for clazz in all_models():
        sync_table(clazz)
