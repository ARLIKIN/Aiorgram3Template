from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_yes_no_kb() -> InlineKeyboardMarkup:
   kb = InlineKeyboardBuilder()
        kb.button(text='Да', callback_data='none')
        kb.button(text='Нет', callback_data='none')
    kb.adjust(1)
    return kb.as_markup()
