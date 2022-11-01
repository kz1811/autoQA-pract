import psycopg2
from framework.utils.config_parser import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PostgreSqlClient:

    def __init__(self):
        self.user = ConfigParser().get_config()['user']
        self.password = ConfigParser().get_config()['password']
        self.host = ConfigParser().get_config()['host']
        self.port = ConfigParser().get_config()['port']
        self.db_name = ConfigParser().get_config()['database_name']
        self.connection = None
        self.cursor = None
        self.post_query = None

    def connect(self):
        self.connection = psycopg2.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.password,
                                          database=self.db_name
                                          )
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, fetch=False):
        cursor = self.cursor
        cursor.execute(query)
        self.connection.commit()

        if fetch:
            return cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
