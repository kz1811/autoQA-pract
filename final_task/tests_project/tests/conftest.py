from framework.browser.browser import Browser
from framework.sql.client_mysql import MySqlClient
import pytest
from tests_project.steps.steps import Steps


@pytest.fixture(scope='function', autouse=True)
def setup_driver():
    browser = Browser()
    browser.set_up_driver()
    url = Steps().get_authorize_url()
    browser.set_url(url)
    browser.maximize()
    yield browser.get_driver()
    browser.quit()


@pytest.fixture(scope='session')
def mysql_client() -> MySqlClient:
    client = MySqlClient()
    client.connect()
    yield client
    client.cursor.close()
    client.connection.close()
