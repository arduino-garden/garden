from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from db.constants import db_keyspace
import sys
import inspect


class Plant(Model):
    __table_name__ = "plants"
    __keyspace__ = db_keyspace
    id = columns.UUID(primary_key=True)
    name = columns.Text()


class Pot(Model):
    __table_name__ = "pots"
    __keyspace__ = db_keyspace
    id = columns.UUID(primary_key=True)


class Measurement(Model):
    __table_name__ = "measurements"
    __keyspace__ = db_keyspace
    id = columns.UUID(primary_key=True)
    event_timestamp = columns.BigInt()
    temperature = columns.Integer()
    air_moisture = columns.Integer()
    soil_moisture = columns.Integer()
    light = columns.Integer()


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
