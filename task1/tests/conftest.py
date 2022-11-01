from framework.browser.browser import Browser
import pytest
from framework.utils.config_parser import ConfigParser


@pytest.fixture(scope='function', autouse=True)
def setup_driver():
    browser = Browser()
    browser.set_up_driver()
    browser.set_url(ConfigParser().get_config()['host'])
    browser.maximize()
    yield browser.get_driver()
    browser.quit()
