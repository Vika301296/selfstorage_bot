from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Правила")
async def location_determination(callback: types.CallbackQuery):
    rules_text = """
    Правила хранения:
    1. Пункт 1
    2. Пункт 2
    3. Пункт 3
    [Подробнее...](https://cherdak.io/legal/offer/)
    Продолжая использовать сервис, вы подтверждаете, что ознакомились с правилами сервиса и согласны с ними.
    """
    await callback.message.answer(rules_text)
    # builder = InlineKeyboardBuilder()
    # builder.row(types.InlineKeyboardButton(
    #     text="Согласен", callback_data="Согласен")
    # )
    # await callback.message.answer("Нажимая \"Согласен\" Вы подтверждаете согласие с правилами сервиса.",
    #                               reply_markup=builder.as_markup())
