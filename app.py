import asyncio

from handlers.users import start, feedback, back, menu, settings
from loader import dp, bot
from loader import i18n


import handlers
from main.database import database
from middlewares.languages import LanguageMiddleware
from utils.notify_admins import send_notify_dev
from utils.set_bot_command import set_default_commands


async def main():
   dp.include_router(router=start.router)
   dp.include_router(router=feedback.router)
   dp.include_router(router=back.router)
   dp.include_router(router=menu.router)
   dp.include_router(router=settings.router)



   dp.message.middleware(middleware=LanguageMiddleware(i18n=i18n))

   await database.connect()
   await set_default_commands(bot=bot)
   await send_notify_dev(bot=bot)

   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())