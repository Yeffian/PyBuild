from dearpygui.core import *
from dearpygui.simple import *


class Themes:
	dark = "Dark"
	light = "Light"
	classic = "Classic"
	dark2 = "Dark 2"
	grey = "Grey"
	dark_grey = "Dark Grey"
	cherry = "Cherry"
	purple = "Purple"
	gold = "Gold"
	red = "Red"


set_main_window_size(500, 500)
set_main_window_title("PyBuild")
set_theme(Themes.classic)
set_style_window_padding(15, 15)

def _create_project(sender, data):
	...

def create_new_project_dialog():
	with window("Project Manager", width=485, height=480):
		set_window_pos("Project Manager", 0, 0)
		add_input_text("Project name", width=350, default_value="Hello, world!")
		add_button("Create", callback=_create_project)

def start_gui():
	create_new_project_dialog()
	start_dearpygui()
