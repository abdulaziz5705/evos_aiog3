from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputFile
from keyboards.default.users import main_menu_keyboard, category_kb, product_kb
from aiogram import Router, F
import handlers, middlewares, filters
from loader import _, bot


router = Router()

@router.message(F.text.in_(["Menu 🌯", "Menu 🌯", "Меню 🌯"]))
async def main_menu_handler(message: Message):
    text = _("Siz menuni tanladingiz")
    await message.answer(text=text, reply_markup= await main_menu_keyboard())


@router.message(F.text.in_(["Lokatsiya junatish 📍", "Отправить мой лакатсию 📍", "Send my location 📍"]))
async def main_menu_handler(message: Message, state: FSMContext):
    text = _("Lokatsiya junatish")
    await message.answer(text=text, reply_markup= await category_kb())
    await state.clear()

@router.message(F.text == "Burger")
async def send_burger_photo(message: Message):
    text = "Products"
    await message.answer(text=text, reply_markup= await product_kb())