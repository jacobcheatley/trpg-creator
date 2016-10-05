import json

try:
    with open('config.json', mode='r') as in_file:
        config_data = json.load(in_file)
except FileNotFoundError:
    config_data = {}
    with open('config.json', mode='w') as out_file:
        out_file.write('{}')


def get(name):
    if name in config_data:
        return config_data[name]
    else:
        return None


def set(name, value):
    config_data[name] = value
    with open('config.json', mode='w') as out_file:
        json.dump(config_data, out_file)
