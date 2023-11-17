import json
from aiogram.filters.command import Command
from selfstorage.bot.loader import dp, bot
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from selfstorage.bot.utils.set_bot_commands import set_bot_commands

import requests

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await set_bot_commands(bot)
    builder = InlineKeyboardBuilder()

    django_url = "http://127.0.0.1:8000/bot"
    response = requests.get(django_url)
    
    data_from_db = {}  # Provide a default value
    
    if response.status_code == 200:
        try:
            data_from_db = response.json()
            print(data_from_db)
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON: Empty response or invalid JSON format.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    builder.row(types.InlineKeyboardButton(
        text="Правила хранения", callback_data="Правила")
    )
    builder.row(types.InlineKeyboardButton(
        text="Заказать бокс", callback_data="Заказать бокс")
    )
    builder.row(types.InlineKeyboardButton(
        text="Адреса боксов", callback_data="Адреса")
    )
    builder.row(types.InlineKeyboardButton(
        text="Мои вещи", callback_data="Мои вещи")
    )
    await message.answer(
        "Рады видеть <b>Вас</b> в нашем боте!\n"
        "Он поможет <b>Вам</b> без труда сдать на хранение,\n"
        "забрать <b>Ваши</b> вещи,\n"
        "а так же напомнит о том, что храниться у <b>Вас</b> из вещей!"
        f"\n\nData from Django: {data_from_db}",
        reply_markup=builder.as_markup())

@dp.callback_query(F.data == "Старт")
async def start(callback: types.CallbackQuery):
    await set_bot_commands(bot)
    builder = InlineKeyboardBuilder()

    django_url = "http://127.0.0.1:8000/bot/bot_command/"
    response = requests.get(django_url)

    data_from_db = {}  # Provide a default value

    if response.status_code == 200:
        try:
            data_from_db = response.json()
            print(data_from_db)
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON: Empty response or invalid JSON format.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    builder.row(types.InlineKeyboardButton(
        text="Правила хранения", callback_data="Правила")
    )
    builder.row(types.InlineKeyboardButton(
        text="Заказать бокс", callback_data="Заказать бокс")
    )
    builder.row(types.InlineKeyboardButton(
        text="Адреса боксов", callback_data="Адреса")
    )
    builder.row(types.InlineKeyboardButton(
        text="Мои вещи", callback_data="Мои вещи")
    )
    await callback.message.answer(
        "Рады видеть <b>Вас</b> в нашем боте!\n"
        "Он поможет <b>Вам</b> без труда сдать на хранение,\n"
        "забрать <b>Ваши</b> вещи,\n"
        "а так же напомнит о том, что храниться у <b>Вас</b> из вещей!"
        f"\n\nData from Django: {data_from_db}",
        reply_markup=builder.as_markup())
