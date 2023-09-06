from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#admin_menu
first_admin_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Посмотреть данные'),
        KeyboardButton(text='Редактировать данные'),
        KeyboardButton(text='Добавить данные'),
        KeyboardButton(text='Удалить данные'),
    ]
], resize_keyboard=True, row_width=2
)
