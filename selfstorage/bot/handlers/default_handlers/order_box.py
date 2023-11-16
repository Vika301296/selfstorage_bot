from selfstorage.bot.loader import dp
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder


@dp.callback_query(F.data == "Заказать бокс")
async def location_determination(callback: types.CallbackQuery):
    # markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    # registered = запрос к бд есть ли пользователь в бд !!!
    registered = False
    if registered:
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
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Адреса боксов", callback_data="Адреса боксов")
        )
        builder.row(types.InlineKeyboardButton(
            text="Заберём сами", callback_data="Заберём")
        )
        builder.row(types.InlineKeyboardButton(
            text="Назад", callback_data="Старт")
        )
        await callback.message.answer("Выберите адрес склада или мы можем забрать вещи сами!",
                                      reply_markup=builder.as_markup())


@dp.callback_query(F.data == "Адреса боксов")
async def location_determination(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="1. Ленина 56", callback_data="Ленина 56")
    )
    builder.row(types.InlineKeyboardButton(
        text="2. Суздальский 32", callback_data="Суздальский 32")
    )
    builder.row(types.InlineKeyboardButton(
        text="3. Хакурате 325", callback_data="Хакурате 325")
    )
    builder.row(types.InlineKeyboardButton(
        text="4. Митина 12", callback_data="Митина 12")
    )
    builder.row(types.InlineKeyboardButton(
        text="5. Садовая 281", callback_data="Садовая 281")
    )
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Заказать бокс")
    )
    await callback.message.answer("Выберите адрес бокса",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data == "Заберём")
async def location_determination(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="1,5м.кв", callback_data="1,5м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="2м.кв", callback_data="2м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="3м.кв", callback_data="3м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="4м.кв", callback_data="4м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="5м.кв", callback_data="5м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="10м.кв", callback_data="10м.кв")
    )
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Заказать бокс")
    )
    await callback.message.answer("Выберите размер бокса",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data.in_(["1,5м.кв", "2м.кв", "3м.кв", "4м.кв", "5м.кв", "10м.кв"]))
async def location_determination(callback: types.CallbackQuery):
    box_size = callback.data
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Заберём")
    )
    await callback.message.answer(f"Вы выбрали {box_size}",
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data.in_(["Ленина 56", "Суздальский 32", "Хакурате 325", "Митина 12", "Садовая 281"]))
async def location_determination(callback: types.CallbackQuery):
    address_box = callback.data
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Назад", callback_data="Адреса боксов")
    )
    await callback.message.answer(f"Вы выбрали {address_box}",
                                  reply_markup=builder.as_markup())
