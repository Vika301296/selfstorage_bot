import asyncio
import os
from datetime import date
import logging
from django_cron import CronJobBase, Schedule
from selfstorage.bot.models import User
from selfstorage.bot.views import get_expiry_message
from aiogram import Bot, Dispatcher, types


token = os.getenv('BOT_TOKEN')


class CheckLeaseDatesCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'selfstorage.bot.tasks.CheckLeaseDatesCronJob'

    async def send_message_to_user(self, telegram_id, message):
        # Send the message using aiogram
        await self.dp.bot.send_message(
            telegram_id, message, parse_mode=types.ParseMode.MARKDOWN)

    def do(self):
        bot = Bot(token=token)
        self.dp = Dispatcher(bot)
        logging.info("Cron job started")
        today = date.today()
        users = User.objects.all()

        for user in users:
            message = get_expiry_message(user, today)
            asyncio.get_event_loop().run_until_complete(
                self.send_message_to_user(user.telegram_id, message)
            )
        logging.info("Cron job finished")
