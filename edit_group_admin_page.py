import tkinter.ttk
from page import Page
from window_settings import *
from test_data import *


class EditGroup(Page):
    def __init__(self, window, controller):
        self.main_frame = None
        self.num_class = None
        self.teacher = None
        self.teacher_box = None

        self.current_teacher_id = tkinter.IntVar(value=-1)
        super().__init__(window, controller)

    def __str__(self):
        return 'EditGroup'

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self, student_list=None, teacher=None):
        if isinstance(student_list, list):

            self.main_frame = self.create_main_frame(self.main_frame)
            self.teacher = tkinter.Label(self.main_frame,
                                         text=f'Класний керівник: {teacher[0]}',
                                         font=(L_FONT, L_FONT_SIZE))

            self.current_teacher_id.set(teacher[1])


            self.main_frame.pack(side=tkinter.TOP)
            self.teacher.pack(pady=L_PAD_Y)

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
                font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR, command=self.open_change_teacher
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

    def get_current_teacher_id(self):

        return self.current_teacher_id.get()


    def open_change_teacher(self):
        self.window_teacher = tkinter.Tk()
        self.window_teacher.geometry(W_GEOMETRY)

        teacher_list = self.controller.get_teachers()
        only_teachers = []
        for i in teacher_list.keys():
            only_teachers.append(i)

        selected_teacher = tkinter.StringVar()


        self.teacher_box = tkinter.ttk.Combobox(self.window_teacher, values=only_teachers, state='readonly',
                                                width=50, textvariable=selected_teacher)

        button_change = tkinter.Button(
            self.window_teacher, text=f'Змінити класного керівника для класу {self.get_class_number()}', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR,
            command=lambda: self.controller.change_class_teacher(teacher_list[self.teacher_box.get()]))

        self.teacher_box.pack(pady=L_PAD_Y)
        button_change.pack()


    def close_change_teacher_window(self):
        self.window_teacher.destroy()