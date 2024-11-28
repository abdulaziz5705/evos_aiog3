from aiogram import types, Bot

from loader import bot


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Start to use bot 🚀️️️️️️"),
            types.BotCommand(command="help", description="Find all features 🤖"),
            types.BotCommand(command="feedback", description="Send feedback to admin 📝"),
        ]
    )