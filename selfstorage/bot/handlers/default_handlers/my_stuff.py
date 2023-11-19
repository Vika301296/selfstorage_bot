import json
import requests
from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Мои вещи")
async def location_determination(callback: types.CallbackQuery):
    tg_id = callback.from_user.id
    my_belongings_url = 'http://127.0.0.1:8000/bot/my_belongings/'
    check_registration_url = "http://127.0.0.1:8000/bot/check_registration/"
    data = {'telegram_id': tg_id}

    check_registration_response = requests.post(
        check_registration_url, json=data)
    belongings_response = requests.post(my_belongings_url, json=data)

    registration_status = {}
    belongings = []

    if check_registration_response.status_code == 200:
        try:
            registration_status = check_registration_response.json()
            print(registration_status)
        except json.decoder.JSONDecodeError:
            print(
                "Error decoding JSON: Empty response or invalid JSON format.")
    else:
        print(f"Error: {check_registration_response.status_code}"
              f" - {check_registration_response.text}")

    if belongings_response.status_code == 200:
        try:
            belongings = belongings_response.json()
            print(belongings)
        except json.decoder.JSONDecodeError:
            print(
                "Error decoding JSON: Empty response or invalid JSON format.")
    else:
        print(f"Error: {belongings_response.status_code}"
              f" - {belongings_response.text}")

    registered = registration_status.get('registered', False)

    if not registered:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Назад", callback_data="Старт")
        )
        builder.row(types.InlineKeyboardButton(
            text="Регистрация", callback_data="Регистрация")
        )
        await callback.message.answer(
            "Вам необходимо пройти регистрацию",
            reply_markup=builder.as_markup())
    else:
        belongings_str = ', '.join(belongings)
        await callback.message.answer(f"Вещи на хранении: {belongings_str}")
