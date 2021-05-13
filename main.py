from configsetup import setup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--setup", help="Use PyBuild to bootstrap your python project and generate a pyconfig file.", action="store_true")
parser.add_argument("-i", "--install", help="Use PyBuild to update your project dependencies.", action="store_true")
args = parser.parse_args()

if args.setup:
    setup()
