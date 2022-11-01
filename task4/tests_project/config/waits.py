from framework.utils.config_parser import ConfigParser

CONFIG = ConfigParser().get_config()


class Waits(object):
    IMPLICITLY_WAIT_SEC = CONFIG['implicitly_wait_sec']
    PAGE_LOAD_TIMEOUT_SEC = CONFIG['page_load_timeout_sec']
    SCRIPT_TIMEOUT_SEC = CONFIG['script_timeout_sec']
    EXPLICITLY_WAIT_SEC = CONFIG['explicitly_wait_sec']
