import tkinter

from test_data import CLASS_QUANTITY
from window_settings import *


class Page:
    def __init__(self, window, controller):
        self.main_window = window

        self.controller = controller

        self.show_page()

    def __str__(self):
        return 'Page'

    def __del__(self):
        print('Closing page')
        print()

        self.hide_page()

    def set_controller(self, controller):
        self.controller = controller

    def show_page(self):
        self.show_left_panel()
        self.show_main_panel()

    def show_left_panel(self):
        pass

    def show_main_panel(self):
        pass

    def hide_page(self):
        # Усі віджети після індексу 0 є сторінковими віджетами.
        for widget in self.main_window.winfo_children()[1:]:
            widget.destroy()

    def show_groups_in_left_panel(self):
        left_panel = tkinter.Frame(self.main_window, bg=L_PANEL_COLOR, width=L_PANEL_WIDTH)

        number_option = tkinter.IntVar(value=1)

        for i in range(CLASS_QUANTITY):
            option = tkinter.Radiobutton(left_panel, text=f'{i + 1} Клас', value=i + 1, bg=L_PANEL_COLOR,
                                         fg=RB_FONT_COLOR,
                                         width=RB_WIDTH, variable=number_option,
                                         font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT))

            option.pack()

        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

    def __on_radiobutton_click(self, value):
        print(value)
