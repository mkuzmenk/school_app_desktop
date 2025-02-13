CLASS_QUANTITY = 11

OPTION_DEFAULT_VALUE = 0

TEACHER_ID_DEFAULT = -1

ROLE_DEFAULT_OPTION = -1

TEACHER_NAME_POS = 0
TEACHER_ID_POS = 1

STUDENT_NAME_POS = 0
STUDENT_EMAIL_POS = 2

WEEKDAYS = (
    'Понеділок',
    'Вівторок',
    'Середа',
    'Четвер',
    "П'ятниця",
    'Субота',
)

WEEKDAYS_DB = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    "Friday",
    'Saturday',
)

REGISTRATION_OPTIONS = (
    'Вчитель',
    'Учень',
)

IS_STAFF_TRUE = 1
IS_STAFF_FALSE = 0

IS_ACTIVE_TRUE = 1
IS_ACTIVE_FALSE = 0

IS_SUPERUSER_TRUE = 1
IS_SUPERUSER_FALSE = 0

ADMIN_ROLE_ID = 1
TEACHER_ROLE_ID = 2
STUDENT_ROLE_ID = 3

REGISTRATION_LABELS_TEACHER = (
    'ІПН',
    "І'мя",
    'Прізвище',
    'По-батькові',
    'День народження',
    "Клас*",
    'Пошта',
    'Логін',
    'Номер телефону',
    'Стать',
    'Пароль',
    'Повторіть пароль',
)

REGISTRATION_LABELS_STUDENT = (
    'ІПН*',
    "І'мя",
    'Прізвище',
    'По-батькові',
    'День народження',
    "Клас*",
    'Пошта',
    'Логін',
    'Номер телефону',
    'Стать',
    'Пароль',
    'Повторіть пароль',
)

# POS - Position
LABEL_TAX_POS = 0
LABEL_FIRST_NAME_POS = 1
LABEL_LAST_NAME_POS = 2
LABEL_SURNAME_POS = 3
LABEL_BIRTHDATE = 4
LABEL_GROUP_POS = 5
LABEL_EMAIL_POS = 6
LABEL_LOGIN_POS = 7
LABEL_PHONE_NUMBER_POS = 8
LABEL_SEX_POS = 9
LABEL_PASSWORD_POS = 10
LABEL_PASSWORD_REPEAT_POS = 11

LIST_START_POS = 0

TEXT_START_POS = '1.0'

FIRST_COLUMN = 1
SECOND_COLUMN = 2
THIRD_COLUMN = 3

REGISTRATION_LABELS = (
    REGISTRATION_LABELS_TEACHER,
    REGISTRATION_LABELS_STUDENT,
)

SEARCH_LABELS = (
    "Ім'я",
    'Прізвище',
)

SHOW_MESSAGE_CODES = (
    "Одне або декілька полів пусті.",
    "Некоректні дані.",
    "Користувачів не знайдено.",
    "Паролі не співпадають",
    "Вчителя успішно додано.",
    "Учня/ученицю успішно додано.",
    "Завдання успішно додано",
)

CODE_EMPTY_FIELDS = 0
CODE_INVALID_DATA = 1
CODE_USERS_NOT_FOUND = 2
CODE_PASSWORDS_DONT_MATCH = 3
CODE_TEACHER_ADDED = 4
CODE_STUDENT_ADDED = 5
CODE_TASK_ADDED = 6

SEARCH_FIRST_NAME_POS = 0
SEARCH_LAST_NAME_POS = 1

VALUES = 'values'

STATE = 'state'
DISABLED = 'disabled'
NORMAL = 'normal'

PAGE_STR = 'Page'
EDIT_GROUP_STR = 'Edit Group Page'
SCHEDULE_STR = 'Schedule Page'
ADD_USER_STR = 'Add User Page'
FIND_USER_STR = 'Find User Page'

DB_CONN_NOT_FOUND = 'DB connection is not found'

DATETIME_FORMAT = "%H:%M"
BIRTHDATE_FORMAT = "%Y-%m-%d"

NO_STUDENT_NAME = '**Без імені**'
NO_STUDENT_EMAIL = '**Не вказано**'

NO_TEACHER_NAME = '---'

RCB_GROUP_NOT_DEFINED = 'Не визначено'

CTCB_GROUP_NOT_DEFINED = 'Не визначено'

DISCIPLINES_ID = {
    "Математика": 1,
    "Фізика": 2,
    "Хімія": 3,
    "Біологія": 4,
    "Інформатика": 5,
    "Література": 6,
    "Українська мова": 7,
    "Англійська мова": 8,
    "Історія": 9,
    "Географія": 10,
    "Громадянська освіта": 11,
    "Економіка": 12,
    "Правознавство": 13,
    "Фізична культура": 14,
    "Музичне мистецтво": 15,
    "Образотворче мистецтво": 16,
    "Технології": 17,
    "Астрономія": 18,
    "Екологія": 19,
    "Психологія": 20,
}

MARK_VALUES = {
    'Н/О': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    '11': 11,
    '12': 12
}

ADD_TASK_LABELS = (
    'Клас',
    'Тема завдання',
    'Опис завдання',
    'Час здачі',
)

LABEL_TASK_GROUP_ID_POS = 0
LABEL_TASK_TOPIC_POS = 1
LABEL_TASK_DESCRIPTION_POS = 2
LABEL_TASK_DEADLINE_POS = 3

TASK_DATE_POS = 3
TASK_TIME_POS = 4