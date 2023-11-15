from selfstorage.bot.loader import bot, dp
import asyncio
import selfstorage.bot.handlers


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
