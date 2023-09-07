from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#admin_menu
first_admin_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,keyboard=[
    [
        KeyboardButton(text='Посмотреть данные'),
        KeyboardButton(text='Редактировать данные')
    ],
    [
        KeyboardButton(text='Добавить данные'),
        KeyboardButton(text='Удалить данные'),
    ],
]
)
