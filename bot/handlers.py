from aiogram import types
from database import crud
import logging
from datetime import datetime
from bot.buttons.low_first_menu import first_admin_menu
from bot.buttons.field_buttons import view_data_keyboard
from bot import my_states
from aiogram.fsm.context import FSMContext
# Define the start command handler

#logger = logging.getLogger(__name__)

async def start_handler(message: types.Message, state: FSMContext):
    # Prompt the user to enter their token
    await state.set_state(my_states.ObjectState.GET_DATA)
    await message.answer('Для входа по токену введите команду:\n/войти токен')
    # Set the state to the auth_handler function


#Вход по токену
async def auth_handler(message: types.Message):
    # Check if the token exists in the database
    token = message.text.split(" ")[1]
    user_token = crud.get_token(token=token)

    if user_token:
        user = crud.get_access(token=user_token)
        # Store the user ID in the session
        await message.answer(f'Вы вошли как: {"admin" if user.is_superuser else "It"}\nПод ником: {user.username}', reply_markup=first_admin_menu)
        # Log the user, their access level, and the current date and time
        now = datetime.now()
        #logger.info(f'User {user.username} logged in with access level {"admin" if user.is_superuser else "It"} at {now.strftime("%Y-%m-%d %H:%M:%S")}.')
    else:
        # Increment the number of attempts and store it in the session
        await message.answer('Такого токена нет. Попробуйте еще раз.')
        # Log the failed login attempt
        #logger.warning(f'Failed login attempt for token {token} from user {message.from_user.id}.')
        # Block the user if they have exceeded the maximum number of attempts


#Обработчик нижнего меню
async def low_first_menu_handler(message: types.Message):
    if message.text == 'Посмотреть данные':
        await message.answer('Выберите объект для просмотра', reply_markup=view_data_keyboard)

#Обработчик callback
async def find_objectfrom_name(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(my_states.ObjectState.OBJECT)
    await callback.answer('Введите название объекта')

async def object(message: types.Message, state: FSMContext):
    await state.set_state(my_states.ObjectState.GET_DATA)
    await state.update_data(object=message.text)
    await message.answer('Введите дату')

async def get_object(message: types.Message, state: FSMContext):
    data = await state.get_data()
    object = data['object']
    await message.answer(str(object))
    await state.clear()
