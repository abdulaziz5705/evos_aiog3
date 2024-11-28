import logging
from aiogram import Bot
from loader import bot
from main.config import DEVS


async def send_notify_dev(bot: Bot):
    try:
        for dev in DEVS:
            await bot.send_message(text="Bot start work", chat_id=dev)
    except Exception as e:
        logging.error(f"SEnding Info to Devs{e}")
