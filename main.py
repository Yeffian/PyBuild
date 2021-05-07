from os import path
import subprocess
import sys
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

def install_pkgs():
    try:
     print(f'Installing dependancies for {config["title"]}')
     for pkg in config["dependencies"]:
         subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    except Exception as e:
        print('fatal: Failed to import files')
        print(e)

install_pkgs()