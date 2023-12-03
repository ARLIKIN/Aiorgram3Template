from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def select_type_media() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='GIF 🪄', url='google.com')
    kb.button(text='Картинку 🖼', url='google.com')
    kb.adjust(2)
    return kb.as_markup()
