from fabric.api import task, run
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from db.models import sync_all_tables
from db.constants import db_keyspace


@task
def reset():
    print('Connecting to cluster')
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()

    createKeySpace(session)
    sync_all_tables()


def createKeySpace(session):
    print('Dropping existing keyspace')
    session.execute("DROP KEYSPACE IF EXISTS " + db_keyspace)
    print('Creating keyspace for project')
    session.execute(
        "CREATE KEYSPACE " + db_keyspace + " WITH REPLICATION={'class': 'NetworkTopologyStrategy','datacenter1': 1}")
