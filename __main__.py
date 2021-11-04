import argparse

parser = argparse.ArgumentParser(description="A tool that helps you making a good python application, faster.")
parser.add_argument("-gui", "--gui", help="Runs PyBuild in GUI mode.", action="store_true")
args = parser.parse_args()

if args.gui:
	from gui import start_gui
	start_gui()
