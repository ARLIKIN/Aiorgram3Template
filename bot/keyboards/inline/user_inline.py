from typing import TYPE_CHECKING

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def hello_button(
    i18n: TranslatorRunner
) -> InlineKeyboardMarkup:
    """Функция возвращающая кнопку приветствия"""
    kb = InlineKeyboardBuilder()
    kb.button(
        text=i18n.user.button.hello(),
        callback_data='hello'
    )
    return kb.as_markup()