from aiogram import Router, F
from aiogram.fsm.context import FSMContext

import handlers, middlewares, filters
from aiogram.types import Message

from keyboards.default.users import users_menu_keyboard_with_lang
from loader import _

router = Router()

@router.message(F.text.in_(["Orqaga ⬅️", "Назад ⬅️", "Back ⬅️"]))
async def main_menu_handler(message: Message , state: FSMContext):
    data = await state.get_data()
    language = data.get('language')
    text = _("Quydagilardan  bittasini tanlashingiz mumkun 👇", locale = language)
    await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))



