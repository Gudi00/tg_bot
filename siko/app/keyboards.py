from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

# from app.database.requests import get_categories, get_category_item

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)

# get_number = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Отправить номер', callback_data='get_number')]])

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Интересные факты')],
                                     [KeyboardButton(text='Занимательные вопросы')],
                                     [KeyboardButton(text='Сообщение для Миши')],
                                      [KeyboardButton(text='Рекомендации для разработчика')],
                                     [KeyboardButton(text='Сайт знакомств')]],
                           resize_keyboard=True,
                           input_field_placeholder="Дорогой друг, выбери категорию(●'◡'●)")


interesting_facts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='О создателе', callback_data='about_me')],
    [InlineKeyboardButton(text='Что-то новое', callback_data='something_new')],
    [InlineKeyboardButton(text='Написать своё', callback_data='message_from_friends')],
    [InlineKeyboardButton(text='На главную', callback_data='to_main')]])



# async def categories():
#     all_categories = await get_categories()
#     keyboard = InlineKeyboardBuilder()
#     for category in all_categories:
#         keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
#     keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()


# async def items(category_id):
#     all_items = await get_category_item(category_id)
#     keyboard = InlineKeyboardBuilder()
#     for item in all_items:
#         keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
#     keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()
