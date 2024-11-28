# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# from aiogram.utils.keyboard import ReplyKeyboardBuilder
# from sqlalchemy.orm import sessionmaker
#
# from loader import _
# from main.database import engine
# from main.models import Category
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# async def users_menu_keyboard_with_lang(language: str):
#     markup = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                KeyboardButton(text=_("Menu 🌯", locale=language))
#             ],
#             [
#                 KeyboardButton(text=_("Mening zakazlarim 🛍", locale=language))
#             ],
#             [
#                KeyboardButton(text=_("Fikir qoldirish ✍️",  locale=language)),
#                KeyboardButton(text=_("Sozlamalar ⚙️", locale=language))
#
#             ],
#         ],
#         resize_keyboard=True)
#     return markup
# async def users_menu_keyboard():
#     markup = ReplyKeyboardMarkup(
#         keyboard=
#         [
#             [
#                KeyboardButton(text="Menu 🌯")
#             ],
#             [
#                 KeyboardButton(text="Mening zakazlarim 🛍")
#             ],
#             [
#                KeyboardButton(text="Fikir qoldirish ✍️"),
#                KeyboardButton(text="Sozlamalar ⚙️")
#
#             ],
#         ],
#         resize_keyboard=True)
#     return markup
# async def main_menu_keyboard():
#     markup = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=_("Mening manzilim 🗺 "))
#             ],
#             [
#                KeyboardButton(text=_("Lokatsiya junatish 📍")),
#                KeyboardButton(text=_("Orqaga ⬅️"))
#
#             ],
#         ], resize_keyboard=True
#     )
#     return markup
#
# async def settings_keyboard():
#     markup = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=_("Tilni o'zgartirish"))
#             ],
#             [
#                 KeyboardButton(text=_("Orqaga ⬅️"))
#             ]
#         ], resize_keyboard=True
#     )
#     return markup
#
# async def feedbact_keyboard():
#     markup = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=_("Xabarni Yuborish"))
#             ],
#             [
#                 KeyboardButton(text=_("Orqaga ⬅️"))
#             ]
#         ], resize_keyboard=True
#     )
#     return markup
#
# languages = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="🇺🇿 Uzbek"),
#             KeyboardButton(text="🇷🇺 Russian"),
#             KeyboardButton(text="🇬🇧 English"),
#         ]
#     ], resize_keyboard=True
# )
#
#
# async def category_kb():
#     categories = session.query(Category.name).all()
#     builder = ReplyKeyboardBuilder()
#     first_row = [
#         KeyboardButton(text=_("Orqaga ⬅️")),
#         KeyboardButton(text=_("Aksiyalar 💥")),
#         KeyboardButton(text=_("Savat 📥"))
#     ]
#     builder.row(*first_row)
#
#     temp_buttons = list()
#     for cat in categories:
#         temp_buttons.append(KeyboardButton(text=cat))
#         if len(temp_buttons) == 2:
#             builder.row(*temp_buttons)
#             temp_buttons.clear()
#     builder.row(*temp_buttons)
#     keyboard = builder.as_markup(resize_keyboard=True)
#     return keyboard
#
from pkgutil import get_data

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sqlalchemy.orm import sessionmaker

from loader import _  # Ensure the localization loader is properly configured
from main.database import engine
from main.models import Category

Session = sessionmaker(bind=engine)
session = Session()


async def users_menu_keyboard_with_lang(language: str):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Menu 🌯", locale=language))
            ],
            [
                KeyboardButton(text=_("Mening zakazlarim 🛍", locale=language))
            ],
            [
                KeyboardButton(text=_("Fikir qoldirish ✍️", locale=language)),
                KeyboardButton(text=_("Sozlamalar ⚙️", locale=language))
            ],
        ],
        resize_keyboard=True
    )
    return markup


async def users_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Menu 🌯")
            ],
            [
                KeyboardButton(text="Mening zakazlarim 🛍")
            ],
            [
                KeyboardButton(text="Fikir qoldirish ✍️"),
                KeyboardButton(text="Sozlamalar ⚙️")
            ],
        ],
        resize_keyboard=True
    )
    return markup


async def main_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Mening manzilim 🗺"))
            ],
            [
                KeyboardButton(text=_("Lokatsiya junatish 📍")),
                KeyboardButton(text=_("Orqaga ⬅️"))
            ],
        ],
        resize_keyboard=True
    )
    return markup


async def settings_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Tilni o'zgartirish"))
            ],
            [
                KeyboardButton(text=_("Orqaga ⬅️"))
            ]
        ],
        resize_keyboard=True
    )
    return markup


async def feedbact_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Xabarni yuborish"))
            ],
            [
                KeyboardButton(text=_("Orqaga ⬅️"))
            ]
        ],
        resize_keyboard=True
    )
    return markup


languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇷🇺 Russian"),
            KeyboardButton(text="🇬🇧 English"),
        ]
    ],
    resize_keyboard=True
)


async def category_kb():
    categories =["Burger", "Lavash", "Shaurma", "Sub", "Setlar va juftliklar", "Sneklar"]

    builder = ReplyKeyboardBuilder()


    first_row = [
        KeyboardButton(text=_("Orqaga ⬅️")),
        KeyboardButton(text=_("Aksiyalar 💥")),
        KeyboardButton(text=_("Savat 📥"))
    ]
    builder.row(*first_row)

    temp_buttons = []
    for cat in categories:
        temp_buttons.append(KeyboardButton(text=cat))
        if len(temp_buttons) == 2:
            builder.row(*temp_buttons)
            temp_buttons.clear()

    if temp_buttons:
        builder.row(*temp_buttons)

    keyboard = builder.as_markup(resize_keyboard=True)
    return keyboard

async def product_kb():
    categories =["Burger big", "Burger small", "Black burger"]

    builder = ReplyKeyboardBuilder()


    first_row = [
        KeyboardButton(text=_("Orqaga ⬅️")),
        KeyboardButton(text=_("Savat 📥"))
    ]
    builder.row(*first_row)

    temp_buttons = []
    for cat in categories:
        temp_buttons.append(KeyboardButton(text=cat))
        if len(temp_buttons) == 2:
            builder.row(*temp_buttons)
            temp_buttons.clear()

    if temp_buttons:
        builder.row(*temp_buttons)

    keyboard = builder.as_markup(resize_keyboard=True)
    return keyboard
