from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buttons = [
        [
            InlineKeyboardButton(
                text='Фильтр по имени объекта', 
                callback_data='filter_object_name',
                ),
        ],
        [
            InlineKeyboardButton(
                text='Фильтр по клиенту', 
                callback_data='filter_from_client'
                ),
        ],

    ]

view_data_keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons,
        resize_keyboard=True,
        )
