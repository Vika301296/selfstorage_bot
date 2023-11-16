from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Адреса")
async def address_boxes(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Заказать бокс", callback_data="Заказать бокс")
    )
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Старт")
    )
    await callback.message.answer("<b>Список адресов:</b>\n"
                                  "\n1. <u>Ленина 56</u>\n"
                                  "2. <u>Суздальский 32</u>\n"
                                  "3. <u>Хакурате 325</u>\n"
                                  "4. <u>Митина 12</u>\n"
                                  "5. <u>Садовая 281</u>", reply_markup=builder.as_markup())
