from aiogram.types import FSInputFile
from selfstorage.bot.loader import dp, bot
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Регистрация")
async def location_determination(callback: types.CallbackQuery):
    input_file = FSInputFile('documentation\coglasie_na_obrabotku_personalnyh_dannyh.pdf')
    await bot.send_document(callback.from_user.id, document=input_file,
                            caption="Документ о персональных данных")
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Заказать бокс")
    )
    builder.row(types.InlineKeyboardButton(
        text="Согласен", callback_data="Согласен")
    )
    await callback.message.answer("Вы получили файл о согласии на обработку персональных данных.\n"
                                  "Нажимая \"Согласен\" Вы подтверждаете подписание документа.",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data == "Согласен")
async def location_determination(callback: types.CallbackQuery):
    keyboard = [
        [types.KeyboardButton(text="📱 Отправить", request_contact=True)],
        [types.KeyboardButton(text="Назад")]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await callback.message.answer("Нажмите на кнопку ниже, чтобы отправить контакт", reply_markup=markup)


@dp.message(F.contact)
async def location(message: types.Message):
    name = f"{message.from_user.first_name}"
    phone = message.contact.phone_number
    await message.answer(f"Спасибо, {name}.\n"
                         f"Ваш номер {phone} был получен",
                         reply_markup=types.ReplyKeyboardRemove())
    # запрос в бд на регистрацию пользователя !!!
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Заказать бокс", callback_data="Заказать бокс")
    )
    await message.answer(f"Вы зарегистрированы!",
                         reply_markup=builder.as_markup())
