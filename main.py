import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from config.config import TOKEN
from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from database import crud
from datetime import datetime
from buttons import field_buttons, low_first_menu, view_data_menu
#Set up logging

# Set up the bot and dispatcher
TOKEN = str(TOKEN)
router = Router()

class UserState(StatesGroup):
    USER_TOKEN = State()
    USRE_NAME = State()
    USER_ROLE = State()


class LowtMenu(StatesGroup):
    FIRST_MENU = State()
    SECOND_MENU = State()
    THIRD_MENU = State()

class TypeMenu(StatesGroup):
    VIEW_TYPE = State()
    UPDATE_TYPE = State()
    ADD_TYPE = State()
    DELETE_TYPE = State()


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await state.set_state(UserState.USER_TOKEN)
    await message.answer('Для входа по токену введите токен')

@router.message(UserState.USER_TOKEN)
async def auth(message: types.Message, state: FSMContext):
    # Check if the token exists in the database
    user_token = crud.get_token(token=str(message.text))
    if user_token:
        user = crud.get_access(token=user_token)
        await state.set_state(LowtMenu.FIRST_MENU)
        await state.update_data(user_name=user.username)
        await state.update_data(user_token=user_token)
        await state.update_data(user_role=user.is_superuser)
        await message.answer(f'Вы вошли как: {"admin" if user.is_superuser else "It"}\nПод ником: {user.username}', reply_markup=low_first_menu.first_admin_menu)
    else:
        await message.answer('Такого токена нет. Попробуйте еще раз.')

@router.message(F.text=='Посмотреть данные')
async def admin_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
            'Вы выбрали: смотреть данные', 
            reply_markup=view_data_menu.view_data_admin
            )

@router.message(F.text=='Найти где находится объект')
async def view_data(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
            'Выберите по каким параметрам искать объект',
            reply_markup=field_buttons.view_data_keyboard
            )

@router.callback_query(F.data.startswith('filter_'))
async def filter_data(callback_query: types.CallbackQuery, state: FSMContext):
    user_data = callback_query.data.split('_')[2]
    if user_data == "name":
        await state.update_data(filter_name=str(user_data))
        await state.set_state(TypeMenu.VIEW_TYPE)
        await callback_query.answer('Вы выбрали фильтр по имени объекта')
    elif user_data == "client":
        await state.update_data(filter_client=str(user_data))
        await state.set_state(TypeMenu.VIEW_TYPE)
        await callback_query.answer('Вы выбрали фильтр по клиенту')

@router.message(TypeMenu.VIEW_TYPE)
async def view_type(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    if state_data.get('filter_name') is not None:
        await state.update_data(filter_name=str(message.text))
        results = crud.get_data_from_object(object_enter=str(message.text))
        await message.answer(f"{results[0].object} {results[2].name}")


    elif state_data.get('filter_client') is not None:
        await state.update_data(filter_client=str(message.text))
        #await message.answer(str(results))
    elif state_data.get('filter_name') is not None and state_data.get('filter_client') is not None:
        await message.answer(str(state_data.keys()))
        await state.clear()
    


async def main():
    bot = Bot(token=str(TOKEN), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
