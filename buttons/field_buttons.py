from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


buttons = [
        [InlineKeyboardButton(text='найти объект по названию', callback_data='find_objectfrom_name'),
        InlineKeyboardButton(text='найти объект по логину', callback_data='find_objectfrom_login'),]
        ]

view_data_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=1)
