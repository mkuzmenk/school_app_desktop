import tkinter.ttk
from view.main_windows.Page import Page
from view.main_windows.Window import *
from controller.constants import *


class EditGroup(Page):
    def __init__(self, window, controller):
        self.main_frame = None
        self.num_class = None
        self.table = None

        self.window_teacher = None
        self.window_teacher_box = None

        self.window_student = None
        self.window_student_group_box = None

        self.current_teacher_id = tkinter.IntVar(value=TEACHER_ID_DEFAULT)
        super().__init__(window, controller)

    def __str__(self):
        return EDIT_GROUP_STR

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self, student_list=None, teacher_data=None):
        if isinstance(student_list, list):
            # ?
            self.main_frame = self.create_main_frame(self.main_frame)

            teacher = tkinter.Label(
                self.main_frame,
                text=f'Класний керівник: {teacher_data[TEACHER_NAME_POS]}',
                font=(LA_FONT, LA_FONT_SIZE)
            )

            self.current_teacher_id.set(teacher_data[TEACHER_ID_POS])

            self.main_frame.pack(side=tkinter.TOP)
            teacher.pack(pady=LA_PAD_Y)

            button_frame = tkinter.Frame(
                self.main_frame
            )
            button_frame.pack(side=tkinter.BOTTOM)

            self.table = tkinter.ttk.Treeview(
                self.main_frame, show='headings', columns=('#1', '#2', '#3'), height=TEG_HEIGHT
            )
            self.table.heading('#1', text='ПІБ')
            self.table.heading('#2', text='Дата народження')
            self.table.heading('#3', text='Пошта')

            scrollbar = tkinter.ttk.Scrollbar(
                self.main_frame, orient=tkinter.VERTICAL, command=self.table.yview
            )
            self.table.configure(yscrollcommand=scrollbar.set)

            for student in student_list:
                self.table.insert("", tkinter.END, values=student)

            self.table.pack(side=tkinter.LEFT)
            scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

            change_student_group_button = tkinter.Button(
                button_frame, text='Перевести учня', bg=B_COLOR,
                font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR, command=self.open_change_student_window
            )
            change_student_group_button.pack(side=tkinter.LEFT, padx=B_PAD_X, pady=B_PAD_Y)

            change_student_teacher_button = tkinter.Button(
                button_frame, text='Змінити класного керівника', bg=B_COLOR,
                font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR, command=self.open_change_teacher_window
            )
            change_student_teacher_button.pack(side=tkinter.LEFT, padx=B_PAD_X, pady=B_PAD_Y)

    def show_groups_in_left_panel(self):
        left_panel = tkinter.Frame(self.main_window, bg=LE_PANEL_COLOR, width=LE_PANEL_WIDTH)

        self.num_class = tkinter.IntVar(value=OPTION_DEFAULT_VALUE)
        self.option_dictionary = dict()
        for class_number in range(CLASS_QUANTITY):
            option = tkinter.Radiobutton(
                left_panel, text=f'{class_number + 1} Клас', value=class_number + 1, bg=LE_PANEL_COLOR,
                fg=RB_FONT_COLOR,
                width=RB_WIDTH, variable=self.num_class,
                font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                command=self.controller.show_students
            )

            self.option_dictionary[class_number + 1] = option
            option.pack()

        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

    def create_main_frame(self, frame):
        if frame is not None:
            frame.destroy()

        return tkinter.Frame(self.main_window)

    def get_class_number(self):
        return self.num_class.get()

    def get_current_teacher_id(self):
        old_teacher_id = self.current_teacher_id.get()

        if old_teacher_id == TEACHER_ID_DEFAULT:
            old_teacher_id = None

        return old_teacher_id

    def open_change_teacher_window(self):
        self.window_teacher = tkinter.Tk()
        self.window_teacher.geometry(TW_GEOMETRY)
        self.window_teacher.title(TW_TITLE)

        teacher_list = self.controller.get_teachers()

        only_teachers = []

        for teacher_name in teacher_list.keys():
            only_teachers.append(teacher_name)

        selected_teacher = tkinter.StringVar()

        self.window_teacher_box = tkinter.ttk.Combobox(
            self.window_teacher, values=only_teachers, state=TWCB_STATE,
            textvariable=selected_teacher, width=TWCB_WIDTH,
            font=(TWCB_FONT, TWCB_FONT_SIZE)
        )

        button_change = tkinter.Button(
            self.window_teacher, text=f'Змінити класного керівника для класу {self.get_class_number()}', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR,
            command=lambda: self.controller.change_class_teacher(teacher_list[self.window_teacher_box.get()])
        )

        self.window_teacher_box.pack(pady=TWCB_PAD_Y)
        button_change.pack()

    def open_change_student_window(self):
        selected_student = self.table.selection()

        if selected_student:
            self.window_student = tkinter.Tk()
            self.window_student.geometry(SW_GEOMETRY)
            self.window_student.title(SW_TITLE)

            group_list = self.controller.get_groups()

            selected_group = tkinter.StringVar()

            self.window_student_group_box = tkinter.ttk.Combobox(
                self.window_student, values=group_list, state=SWCB_STATE,
                textvariable=selected_group, width=SWCB_WIDTH,
                font=(SWCB_FONT, SWCB_FONT_SIZE)
            )

            student = self.table.item(selected_student)[VALUES]
            student_name = student[STUDENT_NAME_POS]
            student_email = student[STUDENT_EMAIL_POS]

            button_change = tkinter.Button(
                self.window_student, text=f'Перевести учня {student_name} з {self.get_class_number()} класу',
                bg=B_COLOR, font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR,
                command=lambda: self.controller.change_student(student_email, self.window_student_group_box.get())
            )

            self.window_student_group_box.pack(pady=LA_PAD_Y)
            button_change.pack()
        else:
            self.parent.show_message(CODE_STUDENT_NOT_CHOSEN)

    def close_change_teacher_window(self):
        self.window_teacher.destroy()

    def close_change_student_window(self):
        self.window_student.destroy()
