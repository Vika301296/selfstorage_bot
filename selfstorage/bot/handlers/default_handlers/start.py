from aiogram.filters.command import Command
from selfstorage.bot.loader import dp, bot
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from selfstorage.bot.utils.set_bot_commands import set_bot_commands


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await set_bot_commands(bot)
    builder = InlineKeyboardBuilder()
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
    await message.answer("Рады видеть <b>Вас</b> в нашем боте!\n"
                         "Он поможет <b>Вам</b> без труда сдать на хранение,\n"
                         "забрать <b>Ваши</b> вещи,\n"
                         "а так же напомнит о том, что храниться у <b>Вас</b> из вещей!",
                         reply_markup=builder.as_markup())
