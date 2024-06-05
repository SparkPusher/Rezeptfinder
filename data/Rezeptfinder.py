import dearpygui.dearpygui as dpg
from functions import theme
from Rezeptbuch import Rezeptbuch

class Rezeptfiner():
    def __init__(self):
        rezeptbuch = Rezeptbuch()
        self.interface()

    def interface(self):
        dpg.create_context()
        
        self.font()
        self.primary()
        self.add_rezept_window()
        self.modes()
        self.handler()
        theme()

        self.set_fonts()
        self.auto_align()
        
        dpg.create_viewport(title='Containermessung',
                            width=int(1200),
                            height=int(1000))
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        dpg.destroy_context()

    def primary(self):
        with dpg.window(tag="Primary Window") as self.primary_window:
            self.header = dpg.add_text("Rezeptfinder")
            self.instruction_one = dpg.add_text("Rezept hinzufügen:")
            self.instruction_two = dpg.add_text("Wie soll gesucht werden?")
            # self.checkbox_rezept = dpg.add_combo(['a', 'b', 'c'], default_value="Please Select", width=130) 

    def add_rezept_window(self):
        with dpg.window(no_title_bar=True, no_move=True, no_close=True) as self.rezept_window:
            dpg.add_text("Rezept hinzufügen")
            self.name = dpg.add_input_text(label="Rezeptname", width=200)
            self.book = dpg.add_input_text(label="Kochbuch", width=200)
            self.page = dpg.add_input_text(label="Seite", width=200)
            self.ingredients = dpg.add_input_text(label="Zutaten", width=200)
            dpg.add_button(label="Hinzufügen")    

    def modes(self):
        with dpg.window(no_title_bar=True, no_move=True, no_close=True) as self.tab_window:
            with dpg.tab_bar():
                with dpg.tab(label="Rezept"):
                    dpg.add_text("Rezeptfinder")
                with dpg.tab(label="Zutaten"):
                    dpg.add_text("Zutatenfinder")
                with dpg.tab(label="Rezept"):
                    dpg.add_text("Rezept")

    def set_fonts(self):
        dpg.bind_item_font(self.header, self.fon40)
        dpg.bind_item_font(self.instruction_one, self.fon20)
        dpg.bind_item_font(self.instruction_two, self.fon20)
        dpg.bind_item_font(self.tab_window, self.fon15)

    def handler(self):
        with dpg.item_handler_registry() as item_handler_registry:
            dpg.add_item_resize_handler(callback=self.auto_align)
        dpg.bind_item_handler_registry(self.primary_window, item_handler_registry)
    
    def auto_align(self):
        dpg.configure_item(self.header, pos=[20, 20])
        dpg.configure_item(self.instruction_one, pos=[20, 70]) 
        dpg.configure_item(self.instruction_two, pos=[20, 600]) 
        dpg.configure_item(self.tab_window, pos=[0, 630]) 
        dpg.configure_item(self.tab_window, width=dpg.get_item_width(self.primary_window),
                           height=dpg.get_item_height(self.primary_window)) 
        dpg.configure_item(self.rezept_window, pos=[0, 100], width=dpg.get_item_width(self.primary_window),
                            height=dpg.get_item_height(self.primary_window) - 
                            dpg.get_item_height(self.tab_window) - 100)

    def font(self):
        with dpg.font_registry():
            self.fon15 = dpg.add_font("C:/Windows/Fonts/Calibri.ttf", 15, default_font=True)
            self.fon20 = dpg.add_font("C:/Windows/Fonts/Calibri.ttf", 20, default_font=True)
            self.fon23 = dpg.add_font("C:/Windows/Fonts/Calibri.ttf", 23, default_font=True)
            self.fon25 = dpg.add_font("C:/Windows/Fonts/Calibri.ttf", 25, default_font=True)
            self.fon30 = dpg.add_font("C:/Windows/Fonts/Calibri.ttf", 30, default_font=True)
            self.fon35 = dpg.add_font("C:/Windows/Fonts/Calibri.ttf", 35, default_font=True)
            self.fon40 = dpg.add_font("C:/Windows/Fonts/Calibri.ttf", 40, default_font=True)

# %%
