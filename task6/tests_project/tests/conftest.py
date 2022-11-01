import pytest
from framework.sql.client_sql import PostgreSqlClient


@pytest.fixture(scope='session')
def sql_client() -> PostgreSqlClient:
    client = PostgreSqlClient()
    client.connect()
    yield client

    client.close()


@pytest.fixture(scope='function')
def post_condition_query(sql_client):

    query_list = []

    def query(query_str):
        query_list.append(query_str)

    yield query

    for query_string in query_list:
        sql_client.execute_query(query_string)
