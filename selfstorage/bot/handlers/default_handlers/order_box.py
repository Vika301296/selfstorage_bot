from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests
import json


@dp.callback_query(F.data == "Заказать бокс")
async def location_determination(callback: types.CallbackQuery):
    # markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    # registered = запрос к бд есть ли пользователь в бд !!!
    tg_id = callback.from_user.id
    django_url = "http://127.0.0.1:8000/bot/check_registration/"
    data = {'telegram_id': tg_id}

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

    registered = data_from_db.get('registered', False)

    if not registered:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Назад", callback_data="Старт")
        )
        builder.row(types.InlineKeyboardButton(
            text="Регистрация", callback_data="Регистрация")
        )
        await callback.message.answer("Вам необходимо пройти регистрацию",
                                      reply_markup=builder.as_markup())
    else:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Адреса боксов", callback_data="Адреса боксов")
        )
        builder.row(types.InlineKeyboardButton(
            text="Заберём сами", callback_data="Заберём")
        )
        builder.row(types.InlineKeyboardButton(
            text="Назад", callback_data="Старт")
        )
        await callback.message.answer("Выберите адрес склада или мы можем забрать вещи сами!",
                                      reply_markup=builder.as_markup())


@dp.callback_query(F.data == "Адреса боксов")
async def location_determination(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    django_url = "http://127.0.0.1:8000/bot/storage_address/"

    response = requests.get(django_url)

    addresses = {}
    if response.status_code == 200:
        try:
            addresses = response.json()
            print(addresses)
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON: Empty response or invalid JSON format.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    for address in addresses:
        builder.row(types.InlineKeyboardButton(
            text=f"{address}", callback_data=f"{address}"))

    await callback.message.answer("Выберите адрес бокса",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data == "Заберём")
async def location_determination(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="1,5м.кв", callback_data="1,5м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="2м.кв", callback_data="2м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="3м.кв", callback_data="3м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="4м.кв", callback_data="4м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="5м.кв", callback_data="5м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="10м.кв", callback_data="10м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Заказать бокс")
    )
    await callback.message.answer("Выберите размер бокса",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data.in_(["1,5м.кв", "2м.кв", "3м.кв", "4м.кв", "5м.кв", "10м.кв"]))
async def location_determination(callback: types.CallbackQuery):
    box_size = callback.data
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Заберём")
    )
    await callback.message.answer(f"Вы выбрали {box_size}",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data.in_(["Ленина 56", "Суздальский 32", "Хакурате 325", "Митина 12", "Садовая 281"]))
async def location_determination(callback: types.CallbackQuery):
    address_box = callback.data
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Адреса боксов")
    )
    await callback.message.answer(f"Вы выбрали {address_box}",
                                  reply_markup=builder.as_markup())
