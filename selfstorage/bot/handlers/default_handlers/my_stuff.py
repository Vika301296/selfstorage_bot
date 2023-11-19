import json
import requests
from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Мои вещи")
async def location_determination(callback: types.CallbackQuery):
    tg_id = callback.from_user.id
    url = 'http://127.0.0.1:8000/bot/my_belongings/'
    data = {'telegram_id': tg_id}
    response = requests.get(url, json=data)
    # csrf_token = await dp.storage.get_data(user=callback.from_user.id)
    # headers = {'X-CSRFToken': csrf_token}

    # response = requests.post(url, json=data, headers=headers)
    data_from_db = {}
    if response.status_code == 200:
        try:
            data_from_db = response.json()
            print(data_from_db)
        except json.decoder.JSONDecodeError:
            print(
                "Error decoding JSON: Empty response or invalid JSON format.")
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

        await callback.message.answer(f"Вещи на хранении: {data_from_db}")
