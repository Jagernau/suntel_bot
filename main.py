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
from buttons import field_buttons, low_first_menu 
#Set up logging

# Set up the bot and dispatcher
TOKEN = str(TOKEN)
router = Router()

class UserState(StatesGroup):
    USER_TOKEN = State()
    USRE_NAME = State()
    USER_ROLE = State()


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await state.set_state(UserState.USER_TOKEN)
    await message.answer('Для входа по токену введите токен')

@router.message(UserState.USER_TOKEN)
async def auth(message: types.Message, state: FSMContext):
    # Check if the token exists in the database
    user_token = crud.get_token(token=message.text)
    if user_token:
        user = crud.get_access(token=user_token)
        await state.update_data(user_name=user.username)
        await state.update_data(user_token=user_token)
        await state.update_data(user_role=user.is_superuser)
        await message.answer(f'Вы вошли как: {"admin" if user.is_superuser else "It"}\nПод ником: {user.username}', reply_markup=low_first_menu.first_admin_menu)
    else:
        await message.answer('Такого токена нет. Попробуйте еще раз.')





async def main():
    bot = Bot(token=str(TOKEN), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
