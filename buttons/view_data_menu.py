from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

view_data_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,keyboard=[
    [
        KeyboardButton(text='Найти где находится объект'),
        KeyboardButton(text='Найти на какой системе клиент')
    ],
    [
        KeyboardButton(text='Показать новые терминалы'),
        KeyboardButton(text='Показать изменения объектов'),
    ],
]
)
