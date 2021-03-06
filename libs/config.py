import json


class ConfigLoader:
    data = None

    def __init__(self):
        f = open('config/main.json')
        self.data = json.load(f)
        f.close()

    def get(self, key, default=None):
        if key in self.data:
            return self.data[key]
        else:
            return default

    def get_data(self):
        return self.data

    def dump_config(self):
        print(self.get_data())
