from os import path
import json

CONFIG_FILE_NAME = "pyconfig.json"


def get_config():
    if path.exists(CONFIG_FILE_NAME):
        f = open(CONFIG_FILE_NAME, 'r')
        config = json.load(f)
        return config
    else:
        print('fatal: No pyconfig.json file found.')


config = get_config()
print(f"Project name: {config['title']}")
print(f'Project version: {config["version"]}')
