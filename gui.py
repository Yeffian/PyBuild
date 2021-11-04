import os

import dearpygui.dearpygui as dpg
from os import path


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


dpg.create_context()
dpg.create_viewport(title="PyBuild", width=500, height=500)
dpg.bind_theme(Themes.classic)


def create_new_project_dialog():
	with dpg.window(label="Project Manager", width=585, height=580, no_move=True, pos=(0, 0)):
		dpg.add_input_text(label="Project Name", width=350, default_value="Hello, world!", tag="proj_name")
		dpg.add_input_text(label="Project Location", width=350, default_value="C:/", tag="proj_location")

		dpg.add_button(label="Create", callback=_create_project)




def _create_project(sender, data):
	name = dpg.get_value("proj_name")
	location = dpg.get_value("proj_location")

	if path.isdir(location):
		os.mkdir(location + f'/src')
		os.chdir(location + '/src')
		print(os.getcwd())
	else:
		os.mkdir(location)
		os.mkdir(location + '/src')
		os.chdir(location + '/src')
		print(os.getcwd())


def start_gui():
	dpg.setup_dearpygui()
	create_new_project_dialog()
	dpg.show_viewport()

	while dpg.is_dearpygui_running():
		dpg.render_dearpygui_frame()

	dpg.destroy_context()
