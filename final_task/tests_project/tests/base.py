import pytest
from framework.sql.client_mysql import MySqlClient
from tests_project.sql.sql_union_reporting import SqlUnionReporting


class SqlPrepare:
    builder = None
    postgresql = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MySqlClient = mysql_client
        self.builder: SqlUnionReporting = SqlUnionReporting(self.mysql)
