import pymysql
from framework.utils.config_parser import ConfigParser


class MySqlClient:

    def __init__(self):
        self.user = ConfigParser().get_config()['mysql_creds']['user']
        self.password = ConfigParser().get_config()['mysql_creds']['password']
        self.host = ConfigParser().get_config()['mysql_creds']['host']
        self.port = int(ConfigParser().get_config()['mysql_creds']['port'])
        self.db_name = ConfigParser().get_config()['mysql_creds']['database_name']
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pymysql.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db_name
                                          )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, fetch=False, args=None):
        cursor = self.cursor

        if args is not None:
            cursor.execute(query, args)
        else:
            cursor.execute(query)

        self.connection.commit()
        if fetch:
            return cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
