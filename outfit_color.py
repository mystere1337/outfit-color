import av
import sys
import numpy as np
import dearpygui.dearpygui as dpg #Import the GUI library

input = "please select an input" # Input path

# Callback function used for the input selection button
def input_callback(sender, app_data):
    input = app_data['file_path_name']
    dpg.set_value("test", input)

# Create context for the window
dpg.create_context()

# Add file dialog to open input
with dpg.file_dialog(directory_selector=False, show=False, callback=input_callback, tag="file_dialog_id"):
    dpg.add_file_extension(".mp4", color=(255, 255, 0, 255))

# Create a window item, containing the following items
with dpg.window(tag="window1"):
    with dpg.group(horizontal=True):
        select_input_button = dpg.add_button(label="select input", callback=lambda: dpg.show_item("file_dialog_id"))
        dpg.add_text(input, tag="test")

# Create window
dpg.create_viewport(title='outfit color', width=1200, height=1000)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window1", True) # Bind the window item to the viewport
dpg.start_dearpygui()
dpg.destroy_context()