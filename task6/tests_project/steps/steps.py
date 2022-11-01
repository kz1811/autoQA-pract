from framework.utils.config_parser import ConfigParser
from tests_project.sql.sql_builder import SqlBuilder
from framework.sql.client_sql import PostgreSqlClient
from tests_project.files.test_data import *
from tests_project.files.queries import *


class Steps:

    builder = SqlBuilder(PostgreSqlClient())

    def get_data_from_table(self, postgresql, table=ConfigParser().get_config()['table_name'], limit=TESTS_LIMIT):
        return postgresql.execute_query(GET_DATA_FROM_TABLE_QUERY.format(table, limit), fetch=True)

    def reload_the_tests_from_table(self, funcs, value, table_data, fixture):

        for result in table_data:
            funcs[result[1]](self, post_condition_query=fixture, value=value, query_type='update', test_id=result[0])

    def get_ending_query(self, test_id, name, result, query_type, ):

        result = 'pass' if result else 'fail'

        if query_type is None:
            return self.builder.get_insert_tests_data_query(name=name, project=PROJECT_NAME, result=result)
        elif query_type == 'update':
            return self.builder.get_update_test_query(test_id=test_id, result=result)
        else:
            raise RuntimeError("Query can't be send")
