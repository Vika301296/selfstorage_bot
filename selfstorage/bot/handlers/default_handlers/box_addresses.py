import json
import requests

from html import unescape
from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Адреса")
async def address_boxes(callback: types.CallbackQuery):
    django_url = "http://127.0.0.1:8000/bot/storage_address/"
    response = requests.get(django_url)
    if response.status_code == 200:
        try:
            storage_addresses = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            print(
                "Error decoding JSON: Empty response or invalid JSON format.")
            storage_addresses = []
    else:
        print(f"Error: {response.status_code} - {response.text}")
        storage_addresses = []

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Заказать бокс", callback_data="Заказать бокс")
    )
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Старт")
    )
    formatted_addresses = "\n".join(
        [f"<u>{unescape(address)}</u>" for address in storage_addresses])
    await callback.message.answer(
        f"<b>Список адресов:</b>\n{formatted_addresses}",
        reply_markup=builder.as_markup())
