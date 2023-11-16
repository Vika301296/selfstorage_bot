from .loader import bot, dp
import asyncio
from .handlers.default_handlers import box_addresses, help, my_stuff, order_box, registration, start, storage_rules
import logging
import sys

# sys.path.append("selfstorage/selfstorage_bot")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

logging.basicConfig(level=logging.INFO)
