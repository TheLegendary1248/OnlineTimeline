import dearpygui.dearpygui as dpg
import globals

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Example Window"):
    for i in globals.CONFIG:
        dpg.add_button(label=str(i), width=200, height=200)
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()