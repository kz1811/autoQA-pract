from framework.sql.client_sql import PostgreSqlClient
from tests_project.sql.sql_builder import SqlBuilder
import pytest


class SqlPrepare:
    builder = None
    postgresql = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, sql_client):
        self.postgresql: PostgreSqlClient = sql_client
        self.builder: SqlBuilder = SqlBuilder(self.postgresql)