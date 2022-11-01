from framework.utils.config_parser import ConfigParser
from tests_project.files.queries import *


class SqlBuilder:
    def __init__(self, client):
        self.client = client

    def insert_tests_data(self, name, project, result, table=ConfigParser().get_config()['table_name']):
        query = INSERT_DATA_INTO_TESTS_TABLE_QUERY.format(table, name, project, result)
        self.client.execute_query(query)

    def get_insert_tests_data_query(self, name, project, result, table=ConfigParser().get_config()['table_name']):
        query = INSERT_DATA_INTO_TESTS_TABLE_QUERY.format(table, name, project, result)
        return query

    def get_update_test_query(self, test_id, result, table=ConfigParser().get_config()['table_name']):
        query = UPDATE_TESTS_TABLE_QUERY.format(table, result, test_id)
        return query
