import json


class JsonParser:

    def open_json(self, name):
        with open(f'tests_project/files/{name}.json', 'r') as fd:
            return json.load(fd)

    def get_json(self, name):
        return self.open_json(name)
