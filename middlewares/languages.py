
from aiogram.utils.i18n import I18nMiddleware

from utils.user_commands.users import get_user


async def get_lang(user_id):
    user = await get_user(user_id)
    return user.get('language', 'uz') if user else 'uz'

class LanguageMiddleware(I18nMiddleware):
    async def  get_locale(self, event, data):
        user = getattr(event, 'from_user', data.get('event.from_user'))
        return await get_lang(user.id) if user else 'uz'
