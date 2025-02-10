from tkinter import messagebox

from controller.constants import *
from view.Window import *


class Page:
    def __init__(self, window, controller):
        self.main_window = window

        self.controller = controller

        self.option_dictionary = None
        self.num_class = None

        self.show_page()

    def __str__(self):
        return PAGE_STR

    def __del__(self):
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

        self.num_class = tkinter.IntVar(value=NUM_CLASS_DEFAULT)
        self.option_dictionary = dict()

        for i in range(CLASS_QUANTITY):
            option = tkinter.Radiobutton(left_panel, text=f'{i + 1} Клас', value=i + 1, bg=L_PANEL_COLOR,
                                         fg=RB_FONT_COLOR,
                                         width=RB_WIDTH, variable=self.num_class,
                                         font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT))

            self.option_dictionary[i + 1] = option

            option.pack()

        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

    def show_message(self, code):
        messagebox.showinfo(
            title=MB_FAIL_TITLE, message=SHOW_MESSAGE_CODES[code]
        )

    def hide_main_panel(self):
        # Усі віджети після індексу 1 є віджетами головної панелі.
        for widget in self.main_window.winfo_children()[2:]:
            widget.destroy()

    def enable_options(self):
        for option in self.option_dictionary.values():
            if option[STATE] == DISABLED:
                option[STATE] = NORMAL

    def disable_option(self, num):
        self.option_dictionary[num].configure(state=DISABLED)
