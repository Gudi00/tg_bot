from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboards as kb
import database.requests as rq

router = Router()


class Registration(StatesGroup):
    user_first_name = State()
    user_last_name = State()
    extended_information = State()
    phone_number = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет! Как тебя зовут?")
    await state.set_state(Registration.user_first_name)


@router.message(state=Registration.user_first_name)
async def process_first_name(message: Message, state: FSMContext):
    await state.update_data(user_first_name=message.text)
    await state.set_state(Registration.user_last_name)
    await message.answer('Введите вашу вамилию')


@router.message(state=Registration.user_last_name)
async def process_last_name(message: Message, state: FSMContext):
    await state.update_data(user_last_name=message.text)
    await state.set_state(Registration.extended_information)
    await message.answer('Введите дополнительную информацию о себе')


@router.message(state=Registration.extended_information)
async def extended_information(message: Message, state: FSMContext):
    await state.update_data(extended_information=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer('Отправте совой номер телефона')


@router.message(Registration.phone_number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()

    contact = message.contact
    tg_id = contact.user_id
    phone_number = contact.phone_number
    tg_user_first_name = contact.first_name
    tg_user_last_name = contact.last_name
    time = message.date.now()

    await rq.save_user(tg_id=tg_id, tg_user_first_name=tg_user_first_name,
                       user_first_name=data['user_first_name'], tg_user_last_name=tg_user_last_name,
                       user_last_name=data['user_last_name'], phone_number=phone_number,
                       extended_information=data['extended_information'], time=time)
    await state.clear()
    await message.answer('Вы закончили процесс регистрации', reply_markup=kb.interesting_facts)


# @router.message()
# async def save_message(message: Message):# сохраняет новые интересные факты от пользователя
#         await rq.save_something_new(message.from_user.id, message.text)
#         await message.answer("Сообщение сохранено!")


# @router.message(CommandStart())
# async def cmd_start(message: Message):
#
#     await message.answer('Привет! Тебе стало иннересно узнать мои способности, тогда смотри, но для начала нужно рассказать немного о себе)')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи) Что у вас произошло?')


@router.message(F.text == 'Интересные факты')
async def catalog(message: Message):
    await message.answer('Выберите категорию ^_^', reply_markup=kb.interesting_facts)


@router.callback_query(F.data == 'something_new')
async def something_new(message: Message):
    await message.message.answer('Кристиан Андерсен не мог грамотно написать практически ни одного слова.',
                                 reply_markup=kb.interesting_facts)


@router.callback_query(F.data == 'to_main')
async def to_main(callback: CallbackQuery):
    await callback.answer('Выберите категорию ^_^', reply_markup=kb.main)

# @router.callback_query(F.data == 'get_number', F.contact)
# async def get_number(callback: CallbackQuery):
#     number=message.contact.phone_number
#     await callback.answer(f'Номер успешно отправлен {number}', reply_markup=kb.main)


#процесс регистрации через состояния


#
#
# @router.message(Register.number, F.contact)
# async def register_number(message: Message, state: FSMContext):
#     await state.update_data(number=message.contact.phone_number)
#     data = await state.get_data()
#     await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nНомер: {data["number"]}')
#     await state.clear()

# @router.callback_query(F.data.startswith('category_'))
# async def category(callback: CallbackQuery):
#     await callback.answer('Вы выбрали категорию')
#     await callback.message.answer('Выберите товар по категории',
#                                   reply_markup=await kb.items(callback.data.split('_')[1]))
# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
#                                                            request_contact=True)]],
#                                  resize_keyboard=True)


# @router.callback_query(F.data.startswith('item_'))
# async def category(callback: CallbackQuery):
#     item_data = await rq.get_item(callback.data.split('_')[1])
#     await callback.answer('Вы выбрали товар')
#     await callback.message.answer(f'Название: {item_data.name}
#     \nОписание: {item_data.description}\nЦена: {item_data.price}$')
