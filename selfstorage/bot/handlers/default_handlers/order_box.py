from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Заказать бокс")
async def location_determination(callback: types.CallbackQuery):
    await callback.message.answer("Заказываем бокс")