class Page:
    def __init__(self, window):
        self.main_window = window

        self.show_page()

    def __del__(self):
        print('Closing page')
        print()

        self.hide_page()

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
