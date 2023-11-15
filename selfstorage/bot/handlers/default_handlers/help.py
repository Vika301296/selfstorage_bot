from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command


@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer("Команда <b>/start</b> - запускает бота\n"
                         "Команда <b>/help</b> - вызов помощи\n\n"
                         "Запустив бота Вам необходимо ознакомиться с правилами хранения\n\n"
                         "- Вы можете оставить на хранение вещи,\nнажав \"<u>Заказать бокс</u>\"\n\n"
                         "- Так же Вы можете узнать адреса хранений,\nнажав \"<u>Адреса боксов</u>\"\n\n"
                         "- Узнать список вещей у Вас на хранении можно\nнажав \"<u>Мои вещи</u>\"")
