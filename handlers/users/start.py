from aiogram.filters import Command, StateFilter

import handlers
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType, ReplyKeyboardRemove
from loader import _
from keyboards.default.users import languages, users_menu_keyboard_with_lang
from keyboards.command import phone_number_keyboard
from keyboards.default.users import  settings_keyboard
from aiogram import F, Router
from states.users import RegisterState
from utils.get_lang_code import get_lang_by_text
from utils.get_location import get_full_address
from utils.user_commands.users import get_user, add_user

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    user = await get_user(chat_id=message.chat.id)
    language = await get_lang_by_text(language=message.text)
    await state.update_data(language=language)
    if user:
        text = _("Pastagilardan bittasini tanlashingiz mumkun 👇", locale = language)
        await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))
    else:
        text = "🇺🇿 Tilni tanlang\n 🇬🇧 Select Language\n 🇷🇺 Выберите язык"
        await message.answer(text=text, reply_markup=languages)
        await state.set_state(RegisterState.language)


@router.message(StateFilter(RegisterState.language))
async def language_handler(message: Message, state: FSMContext):
    language = await get_lang_by_text(language=message.text)
    await state.update_data(language=language)
    text = _("Iltimos ismingizni kiriting ", locale=language)
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterState.fullname)

@router.message(StateFilter(RegisterState.fullname))
async def get_fullname_handler(message: Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    data = await state.get_data()
    language = data.get('language')

    text = _("Iltimos pasdagi kontakt ulashish tugmasini bosing 📞", locale = language)

    await message.answer(text=text, reply_markup= await phone_number_keyboard(language=language))
    await state.set_state(RegisterState.phone_number)

@router.message(StateFilter(RegisterState.phone_number), F.content_type== ContentType.TEXT)
async def send_phone_number_handler(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    data = await state.get_data()
    language = data.get('language')
    text = _("❌ Telefon nomer formati xato ", locale = language)
    await message.answer(text=text, reply_markup= await phone_number_keyboard(language=language))
    await state.set_state(RegisterState.phone_number)


@router.message(StateFilter(RegisterState.phone_number), F.content_type==ContentType.CONTACT)
async def send_phone_number_handler(message: Message, state: FSMContext):
        await state.update_data(phone_number=message.contact.phone_number)
        data = await state.get_data()
        language = data.get('language')
        new_user = await add_user(message=message, data=data)
        if new_user:
            text = _("Muvofaqiyatli ro'yhatdan o'ttingiz  ✅ ", locale = language)
            await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))
            text = _("Quydagilardan  bittasini tanlashingiz mumkun 👇", locale = language)
            await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))

        else:
            text = _("Iltimos kiyenroq urunib ko'ring", locale = language)
            await message.answer(text=text)

        await state.clear()



@router.message(F.LOCATION)
async def get_full_location(message: Message):
    address = await get_full_address(latitude=message.location.latitude, longitude=message.location.longitude)
    await message.answer(text=address)


@router.message(F.text.in_(["Change language", "Tilni o'zgartirish", "Изменить язык"]))
async def change_language_handler(message: Message):
    text = "🇺🇿 Tilni tanlang\n 🇬🇧 Select Language\n 🇷🇺 Выберите язык"
    await message.answer(text=text, reply_markup=languages)

@router.message(F.text.in_(["🇷🇺 Russian", "🇺🇿 Uzbek", "🇬🇧 English"]))
async def change_language_handler_user(message: Message):
    text = _("Til o'zgartirildi")
    await message.answer(text=text, reply_markup=await settings_keyboard())