from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from src.db.constants import db_keyspace
import sys
import inspect


class Plant(Model):
    __table_name__ = "plants"
    __keyspace__ = db_keyspace
    plant_id = columns.UUID(primary_key=True)
    name = columns.Text()


class Pot(Model):
    __table_name__ = "pots"
    __keyspace__ = db_keyspace
    pot_id = columns.UUID(primary_key=True)


class Measurement(Model):
    __table_name__ = "measurements"
    __keyspace__ = db_keyspace
    measurement_id = columns.UUID(primary_key=True)
    event_timestamp = columns.BigInt()
    air_temperature = columns.Integer()
    air_humidity = columns.Integer()
    soil_moisture = columns.Integer()
    light = columns.Integer()
    plant_id = columns.UUID()
    pot_id = columns.UUID()


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
