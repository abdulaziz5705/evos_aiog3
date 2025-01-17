from aiogram import Router, F
from aiogram.types import Message,ReplyKeyboardRemove
from keyboards.default.users import  feedbact_keyboard, users_menu_keyboard
from loader import  _
import handlers, middlewares, filters
import os
from dotenv import load_dotenv
load_dotenv()

router = Router()

@router.message(F.text.in_(["Fikir qoldirish ✍️", "Оставить отзыв ✍️", "Add feedback ✍️"]))
async def main_menu_handler(message: Message):
    await message.answer(_("Adminga xabar yuborishingiz mumukun"), reply_markup= await feedbact_keyboard())

messages_for_admin = {}

@router.message(F.text.in_(["Xabarni Yuborish", "Отправить сообщение", "Send message"]))
async def send_message_to_user(message: Message):
    user_id = message.from_user.id
    await message.answer(_("Xabar matnini kiriting:"), reply_markup=ReplyKeyboardRemove())
    messages_for_admin[user_id] = None

@router.message(lambda message: message.from_user.id in messages_for_admin)
async def get_message(message: Message):
    user_id = message.from_user.id
    user_username = message.from_user.username
    user_name = message.from_user.first_name
    user_message = message.text

    messages_for_admin[user_id] = user_message
    text = _("Xabar muvaffaqiyatli yuborildi!")
    await message.answer(text=text, reply_markup=await users_menu_keyboard())

    admin_id = os.getenv("ADMINS")
    await message.bot.send_message(
        chat_id=admin_id,
        text=f"""
             Yangi xabar keldi:\n\n"
             Foydalanuvchi ID: {user_id}"
             Foydalanuvchi Username: {user_username}"
             Foydalanuvchi Name: {user_name}"
             Xabar: {user_message}"""
    )
    messages_for_admin.pop(user_id, None)