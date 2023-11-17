# import os
# from django.conf import settings
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selfstorage_bot.settings')
# django.setup()
# from django.core.asgi import get_asgi_application
# settings.configure()
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# from selfstorage.selfstorage_bot.wsgi import *
from aiogram.types import FSInputFile
from selfstorage.bot.loader import dp, bot
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from selfstorage.bot.models import User
import requests
import json



@dp.callback_query(F.data == "Регистрация")
async def location_determination(callback: types.CallbackQuery):
    # input_file = FSInputFile('documentation\coglasie_na_obrabotku_personalnyh_dannyh.pdf')
    # await bot.send_document(callback.from_user.id, document=input_file,
    #                         caption="Документ о персональных данных")
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Заказать бокс")
    )
    builder.row(types.InlineKeyboardButton(
        text="Согласен", callback_data="Согласен")
    )
    await callback.message.answer("Вы получили файл о согласии на обработку персональных данных.\n"
                                  "Нажимая \"Согласен\" Вы подтверждаете подписание документа.",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data == "Согласен")
async def location_determination(callback: types.CallbackQuery):
    keyboard = [
        [types.KeyboardButton(text="📱 Отправить", request_contact=True)],
        [types.KeyboardButton(text="Назад")]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await callback.message.answer("Нажмите на кнопку ниже, чтобы отправить контакт", reply_markup=markup)


@dp.message(F.contact)
async def location(message: types.Message):
    name = f"{message.from_user.first_name}"
    phone = message.contact.phone_number
    tg_id = message.from_user.id

    django_url = "http://127.0.0.1:8000/bot/create_user/"
    data = {'name': name, 'telegram_id': tg_id, 'phonenumber': phone}

    response = requests.post(django_url, json=data)

    data_from_db = {}
    if response.status_code == 200:
        try:
            data_from_db = response.json()
            print(data_from_db)
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON: Empty response or invalid JSON format.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Заказать бокс", callback_data="Заказать бокс")
    )
    await message.answer(f"{name}, Вы зарегистрированы!",
                         reply_markup=builder.as_markup())