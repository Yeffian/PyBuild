import dearpygui.dearpygui as dpg


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

def _create_project(sender, data):
	...

def create_new_project_dialog():
	with dpg.window(label="Project Manager", width=485, height=480, no_move=True, pos=(0, 0)):
		dpg.add_input_text(label="Project name", width=350, default_value="Hello, world!")
		dpg.add_button(label="Create", callback=_create_project)

def start_gui():
	dpg.setup_dearpygui()
	create_new_project_dialog()
	dpg.show_viewport()

	while dpg.is_dearpygui_running():
		dpg.render_dearpygui_frame()

	dpg.destroy_context()
