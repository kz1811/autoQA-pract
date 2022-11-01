import json


class ConfigParser:
    config = None

    def open_config(self):
        with open(r'tests_project\config\config.json', 'r') as fd:
            self.config = json.load(fd)

    def get_config(self):
        if self.config is None:
            self.open_config()
        return self.config
