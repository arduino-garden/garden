from fabric.api import task, run
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import create_keyspace_simple, drop_keyspace
from db.models import sync_all_tables
from db.constants import db_keyspace, replication_factor


@task
def reset():
    print('Connecting to cluster')
    connection.setup(['127.0.0.1'], db_keyspace, protocol_version=3)
    createKeySpace()
    sync_all_tables()


def createKeySpace():
    print('Dropping existing keyspace')
    drop_keyspace(db_keyspace)
    print('Creating keyspace for project')
    create_keyspace_simple(db_keyspace, replication_factor=replication_factor)
