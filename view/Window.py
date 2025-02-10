import tkinter

from view.admin.admin_window_settings import *


class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.state(MW_STATE)
        self.main_window.title(MW_TITLE)

        self.controller = None
        self.active_window = None
        self.toolbar_panel = None

        self.add_toolbar()

    def start(self):
        self.main_window.mainloop()

    def set_controller(self, controller):
        self.controller = controller

    def add_toolbar(self):
        self.toolbar_panel = tkinter.Frame(
            self.main_window, bg=TB_COLOR, height=TB_HEIGHT
        )
        self.toolbar_panel.pack(side=tkinter.TOP, fill=tkinter.X)

        self.add_toolbar_buttons()

    def add_toolbar_buttons(self):
        pass

    def on_toolbar_button_click(self, page_class):
        if not isinstance(self.active_window, page_class):
            if self.active_window:
                self.active_window.__del__()
                self.active_window = None

            self.active_window = page_class(self.main_window, self.controller)
