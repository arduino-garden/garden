from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import create_keyspace_simple, drop_keyspace, execute
from db.models import sync_all_tables
from db.constants import db_keyspace, replication_factor


class CassandraUtils():

    @staticmethod
    def reset_db():
        print('Connecting to cluster')
        connection.setup(['127.0.0.1'], db_keyspace, protocol_version=3)
        print('Dropping existing keyspace')
        drop_keyspace(db_keyspace)
        print('Creating keyspace for project')
        create_keyspace_simple(
            db_keyspace, replication_factor=replication_factor)
        sync_all_tables()

    @staticmethod
    def init_connection():
        print('Connecting to cluster')
        connection.setup(['127.0.0.1'], db_keyspace, protocol_version=3)
        execute("USE " + db_keyspace + ";")
