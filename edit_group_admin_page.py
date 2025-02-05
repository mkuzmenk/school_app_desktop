import tkinter.ttk
from page import Page
from window_settings import *
from test_data import *


class EditGroup(Page):
    def __init__(self, window, controller):
        self.main_frame = None
        super().__init__(window, controller)

    def __str__(self):
        return 'EditGroup'

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self, student_list=None):
        if student_list:
            self.main_frame = self.create_main_frame(self.main_frame)

            self.main_frame.pack(side=tkinter.TOP)

            button_frame = tkinter.Frame(
                self.main_frame
            )
            button_frame.pack(side=tkinter.BOTTOM)

            table = tkinter.ttk.Treeview(
                self.main_frame, show='headings', columns=('#1', '#2', '#3'), height=TEG_HEIGHT
            )
            table.heading('#1', text='ПІБ')
            table.heading('#2', text='Дата народження')
            table.heading('#3', text='Клас')

            scrollbar = tkinter.ttk.Scrollbar(
                self.main_frame, orient=tkinter.VERTICAL, command=table.yview
            )
            table.configure(yscrollcommand=scrollbar.set)

            for student in student_list:
                table.insert("", tkinter.END, values=student)

            table.pack(side=tkinter.LEFT)
            scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

            change_student_group_button = tkinter.Button(
                button_frame, text='Перевести учня', bg=B_COLOR,
                font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR
            )
            change_student_group_button.pack(side=tkinter.LEFT, padx=B_PAD_X, pady=B_PAD_Y)

            change_student_teacher_button = tkinter.Button(
                button_frame, text='Змінити класного керівника', bg=B_COLOR,
                font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR
            )
            change_student_teacher_button.pack(side=tkinter.LEFT, padx=B_PAD_X, pady=B_PAD_Y)


    def show_groups_in_left_panel(self):
        left_panel = tkinter.Frame(self.main_window, bg=L_PANEL_COLOR, width=L_PANEL_WIDTH)

        self.num_class = tkinter.IntVar(value=0)

        for i in range(CLASS_QUANTITY):
            option = tkinter.Radiobutton(left_panel, text=f'{i + 1} Клас', value=i + 1, bg=L_PANEL_COLOR,
                                         fg=RB_FONT_COLOR,
                                         width=RB_WIDTH, variable=self.num_class,
                                         font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                                         command=self.controller.show_students)

            option.pack()

        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)


    def create_main_frame(self, frame):
        if frame is not None:
            frame.destroy()

        return tkinter.Frame(self.main_window)

    def get_class_number(self):
        return self.num_class.get()